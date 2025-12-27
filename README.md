# 🔍 NickScan

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

Una herramienta rápida y eficiente para buscar la disponibilidad de usernames en múltiples plataformas de redes sociales de forma simultánea.

## ✨ Características

- 🚀 **Escaneo asíncrono**: Búsqueda paralela en múltiples plataformas simultáneamente
- 🎯 **Alta precisión**: Verificación doble mediante status code y análisis de contenido
- 📊 **Resultados organizados**: Salida clara categorizada por estado (encontrado/no encontrado/error)
- 💾 **Exportación**: Guarda los resultados en archivo de texto
- 🔧 **Modular**: Arquitectura limpia y fácilmente extensible
- ⚡ **Rápido**: Escaneo completo en ~10 segundos

## 🌐 Plataformas Soportadas

- GitHub
- Twitter/X
- Instagram
- Reddit
- YouTube
- TikTok
- Twitch
- LinkedIn

## 📋 Requisitos

- Python 3.8 o superior
- aiohttp

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/javierbajamar/NickScan.git
cd NickScan
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt.txt
```

O instalar manualmente:

```bash
pip install aiohttp
```

## 📁 Estructura del Proyecto

```
username_scanner/
├── main.py          # Punto de entrada del programa
├── config.py        # Configuración global
├── scanner.py       # Lógica de escaneo
├── sites.py         # Definición de sitios web
├── utils.py         # Utilidades y formateo
├── requirements.txt # Dependencias
└── README.md        # Este archivo
```

## 💻 Uso

### Uso básico

```bash
python main.py
```

El programa te pedirá que introduzcas el username que deseas buscar:

```
👤 Introduce el username a buscar: ejemplo_usuario
```

### Ejemplo de salida

```
============================================================
 USERNAME SCANNER
============================================================
🔍 Buscando: ejemplo_usuario
📊 Plataformas: 8
⏳ Por favor espera...
============================================================

============================================================
📋 RESULTADOS PARA: ejemplo_usuario
============================================================

✅ ENCONTRADAS:
------------------------------------------------------------
  GitHub          → https://github.com/ejemplo_usuario
  Twitter         → https://twitter.com/ejemplo_usuario
  YouTube         → https://www.youtube.com/@ejemplo_usuario

❌ NO ENCONTRADAS:
------------------------------------------------------------
  Instagram
  Reddit
  TikTok

⚠️  ERROR/TIMEOUT:
------------------------------------------------------------
  LinkedIn (Timeout)
  Twitch (Status code: 403)

============================================================
📊 RESUMEN: 3 encontradas | 3 no encontradas | 2 errores
============================================================

💾 ¿Deseas guardar los resultados? (s/n):
```

## 🔧 Uso Avanzado

### Añadir una plataforma personalizada

Edita `sites.py` y añade tu sitio:

```python
SITES = {
    # ... sitios existentes ...
    "NuevoSitio": SiteConfig(
        url="https://nuevositio.com/user/{}",
        error_msg="Usuario no encontrado"
    )
}
```

### Usar como módulo en otro proyecto

```python
import asyncio
from scanner import UsernameScanner
from sites import get_active_sites

async def buscar_usuario(username):
    sites = get_active_sites()
    scanner = UsernameScanner(sites)
    results = await scanner.scan(username)
    
    # Obtener solo cuentas encontradas
    encontradas = scanner.get_found_accounts()
    
    for cuenta in encontradas:
        print(f"{cuenta.site}: {cuenta.url}")

asyncio.run(buscar_usuario("ejemplo"))
```

### Modificar timeout y configuraciones

Edita `config.py`:

```python
# Timeout para las peticiones (en segundos)
REQUEST_TIMEOUT = 15  # Cambiar de 10 a 15 segundos

# User-Agent personalizado
HEADERS = {
    'User-Agent': 'Tu User-Agent personalizado'
}
```

## 📝 Exportación de Resultados

El programa te ofrece guardar los resultados en un archivo de texto:

```
💾 ¿Deseas guardar los resultados? (s/n): s
💾 Resultados guardados en: scan_ejemplo_usuario.txt
```

El archivo contendrá todas las cuentas encontradas con sus URLs.

## ⚠️ Limitaciones y Consideraciones

- **Rate Limiting**: Algunos sitios pueden limitar el número de peticiones. Usa la herramienta de forma responsable.
- **Falsos Positivos/Negativos**: Aunque el scanner es preciso, algunos sitios pueden devolver resultados inesperados.
- **Cambios en Sitios Web**: Las plataformas pueden cambiar su estructura, lo que podría afectar la detección.
- **Términos de Servicio**: Asegúrate de cumplir con los términos de servicio de cada plataforma.

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

### Ideas para contribuir

- Añadir más plataformas
- Mejorar la detección de usernames
- Añadir tests unitarios
- Crear una interfaz gráfica
- Implementar sistema de logging
- Añadir soporte para proxies

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ⚖️ Disclaimer

Esta herramienta está diseñada para uso educativo y de investigación. Los usuarios son responsables de cumplir con:

- Las leyes de privacidad de su jurisdicción
- Los términos de servicio de cada plataforma
- Las políticas de scraping y rate limiting

**No usar esta herramienta para**:
- Acoso o stalking
- Violación de privacidad
- Actividades ilegales
- Scraping masivo o comercial sin autorización

## 👨‍💻 Autor

[@javierbajamar](https://github.com/javierbajamar)

## 🙏 Agradecimientos

- Inspirado en proyectos similares de OSINT (Open Source Intelligence)
- Agradecimientos a la comunidad de Python y asyncio

## 📞 Contacto

Si tienes preguntas, sugerencias o encuentras algún bug:

- Abre un [Issue](https://github.com/javierbajamar/NickScan/issues)
- Envía un Pull Request
- Contacta por discord: javierbajamar

---

⭐ Si este proyecto te resultó útil, considera darle una estrella en GitHub

**Última actualización**: Diciembre 2025