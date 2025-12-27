"""
Definición de sitios web a escanear.
"""


class SiteConfig:
    """Configuración de un sitio web."""

    def __init__(self, url: str, error_msg: str, enabled: bool = True):
        self.url = url
        self.error_msg = error_msg
        self.enabled = enabled


# Diccionario de sitios disponibles
SITES = {
    "GitHub": SiteConfig(
        url="https://github.com/{}",
        error_msg="Not Found"
    ),
    "Twitter": SiteConfig(
        url="https://twitter.com/{}",
        error_msg="This account doesn't exist"
    ),
    "Instagram": SiteConfig(
        url="https://www.instagram.com/{}",
        error_msg="Sorry, this page isn't available"
    ),
    "Reddit": SiteConfig(
        url="https://www.reddit.com/user/{}",
        error_msg="Sorry, nobody on Reddit goes by that name"
    ),
    "YouTube": SiteConfig(
        url="https://www.youtube.com/@{}",
        error_msg="This page isn't available"
    ),
    "TikTok": SiteConfig(
        url="https://www.tiktok.com/@{}",
        error_msg="Couldn't find this account"
    ),
    "Twitch": SiteConfig(
        url="https://www.twitch.tv/{}",
        error_msg="Sorry. Unless you've got a time machine"
    ),
    "LinkedIn": SiteConfig(
        url="https://www.linkedin.com/in/{}",
        error_msg="Page not found"
    )
}


def get_active_sites():
    """Retorna solo los sitios habilitados."""
    return {name: site for name, site in SITES.items() if site.enabled}


def add_custom_site(name: str, url: str, error_msg: str):
    """Añade un sitio personalizado."""
    SITES[name] = SiteConfig(url, error_msg)
