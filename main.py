"""
Punto de entrada principal del programa.
"""

import asyncio

from scanner import UsernameScanner
from sites import get_active_sites
from utils import ResultPrinter, validate_username, export_results_to_file


def main():
    """Función principal del programa."""
    printer = ResultPrinter()

    # Solicitar username
    username = input("\n👤 Introduce el username a buscar: ").strip()

    # Validar username
    if not validate_username(username):
        printer.print_error("Debes introducir un username válido")
        return

    # Obtener sitios activos
    sites = get_active_sites()

    # Mostrar encabezado
    printer.print_header(username, len(sites))

    # Crear escáner y ejecutar
    scanner = UsernameScanner(sites)
    results = asyncio.run(scanner.scan(username))

    # Mostrar resultados
    printer.print_results(username, results)

    # Preguntar si desea exportar
    export = input("💾 ¿Deseas guardar los resultados? (s/n): ").lower().strip()
    if export == 's':
        export_results_to_file(username, results)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Búsqueda cancelada por el usuario.")
    except Exception as e:
        ResultPrinter.print_error(f"Error inesperado: {e}")
