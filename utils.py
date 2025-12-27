"""
Utilidades y funciones de presentación.
"""

from typing import List

from scanner import ScanResult


class ResultPrinter:
    """Formateador de resultados para la consola."""

    @staticmethod
    def print_header(username: str, total_sites: int):
        """Imprime el encabezado."""
        print(f"\n{'=' * 60}")
        print(f" USERNAME SCANNER")
        print(f"{'=' * 60}")
        print(f"🔍 Buscando: {username}")
        print(f"📊 Plataformas: {total_sites}")
        print(f"⏳ Por favor espera...")
        print(f"{'=' * 60}\n")

    @staticmethod
    def print_results(username: str, results: List[ScanResult]):
        """Imprime los resultados del escaneo."""
        found = [r for r in results if r.found is True]
        not_found = [r for r in results if r.found is False]
        errors = [r for r in results if r.found is None]

        print(f"\n{'=' * 60}")
        print(f"📋 RESULTADOS PARA: {username}")
        print(f"{'=' * 60}\n")

        # Cuentas encontradas
        if found:
            print("✅ ENCONTRADAS:")
            print("-" * 60)
            for result in found:
                print(f"  {result.site:15} → {result.url}")
            print()

        # No encontradas
        if not_found:
            print("❌ NO ENCONTRADAS:")
            print("-" * 60)
            for result in not_found:
                print(f"  {result.site}")
            print()

        # Errores
        if errors:
            print("⚠️  ERROR/TIMEOUT:")
            print("-" * 60)
            for result in errors:
                error_msg = f" ({result.error})" if result.error else ""
                print(f"  {result.site}{error_msg}")
            print()

        # Resumen
        print(f"{'=' * 60}")
        print(f"📊 RESUMEN: {len(found)} encontradas | "
              f"{len(not_found)} no encontradas | {len(errors)} errores")
        print(f"{'=' * 60}\n")

    @staticmethod
    def print_error(message: str):
        """Imprime un mensaje de error."""
        print(f"\n❌ Error: {message}\n")


def validate_username(username: str) -> bool:
    """
    Valida que el username sea correcto.
    """
    if not username or not username.strip():
        return False

    # Puedes añadir más validaciones aquí
    # Por ejemplo: longitud mínima, caracteres permitidos, etc.

    return True


def export_results_to_file(username: str, results: List[ScanResult], filename: str = None):
    """
    Exporta los resultados a un archivo de texto.
    """
    if filename is None:
        filename = f"scan_{username}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Resultados de búsqueda para: {username}\n")
        f.write("=" * 60 + "\n\n")

        found = [r for r in results if r.found is True]

        if found:
            f.write("CUENTAS ENCONTRADAS:\n")
            f.write("-" * 60 + "\n")
            for result in found:
                f.write(f"{result.site}: {result.url}\n")
        else:
            f.write("No se encontraron cuentas.\n")

    print(f"💾 Resultados guardados en: {filename}")
