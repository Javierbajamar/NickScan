"""
Lógica principal de escaneo de usernames.
"""

import asyncio
from typing import Dict, Optional

import aiohttp

from config import HEADERS, REQUEST_TIMEOUT
from sites import SiteConfig


class ScanResult:
    """Resultado del escaneo de un sitio."""

    def __init__(self, site: str, found: Optional[bool], url: str, error: str = None):
        self.site = site
        self.found = found  # True=encontrado, False=no encontrado, None=error
        self.url = url
        self.error = error

    def __repr__(self):
        status = "FOUND" if self.found else "NOT FOUND" if self.found is False else "ERROR"
        return f"<ScanResult {self.site}: {status}>"


class UsernameScanner:
    """Escáner de usernames en múltiples plataformas."""

    def __init__(self, sites: Dict[str, SiteConfig]):
        self.sites = sites
        self.results = []

    async def check_site(self, session: aiohttp.ClientSession,
                         site_name: str, username: str,
                         site_config: SiteConfig) -> ScanResult:
        """
        Verifica si un username existe en un sitio específico.
        """
        url = site_config.url.format(username)

        try:
            async with session.get(
                    url,
                    timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT),
                    allow_redirects=True
            ) as response:

                if response.status == 200:
                    text = await response.text()

                    # Verificar si hay mensaje de error en el contenido
                    if site_config.error_msg.lower() in text.lower():
                        return ScanResult(site_name, False, url)

                    return ScanResult(site_name, True, url)

                elif response.status == 404:
                    return ScanResult(site_name, False, url)

                else:
                    return ScanResult(site_name, None, url,
                                      error=f"Status code: {response.status}")

        except asyncio.TimeoutError:
            return ScanResult(site_name, None, url, error="Timeout")
        except Exception as e:
            return ScanResult(site_name, None, url, error=str(e))

    async def scan(self, username: str) -> list[ScanResult]:
        """
        Escanea todos los sitios de forma asíncrona.
        """
        async with aiohttp.ClientSession(headers=HEADERS) as session:
            tasks = [
                self.check_site(session, site_name, username, site_config)
                for site_name, site_config in self.sites.items()
            ]

            self.results = await asyncio.gather(*tasks)
            return self.results

    def get_found_accounts(self) -> list[ScanResult]:
        """Retorna solo las cuentas encontradas."""
        return [r for r in self.results if r.found is True]

    def get_not_found_accounts(self) -> list[ScanResult]:
        """Retorna las cuentas no encontradas."""
        return [r for r in self.results if r.found is False]

    def get_errors(self) -> list[ScanResult]:
        """Retorna los sitios con error."""
        return [r for r in self.results if r.found is None]
