# 🚀 WWLC - Web Wordlist Creator (v1.1)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Security](https://img.shields.io/badge/security-SSRF--Mitigated-orange.svg)

**WWLC (Web Wordlist Creator)** es una herramienta avanzada de reconocimiento diseñada para generar diccionarios de palabras altamente personalizados a partir de activos web. A diferencia de los scrapers tradicionales, WWLC utiliza automatización de navegador y captura de red para extraer datos de aplicaciones web modernas.

---

## 📋 Tabla de Contenidos
- [Características Principales](#-características-principales)
- [Arquitectura de Seguridad](#-arquitectura-de-seguridad)
- [Instalación Rápida](#-instalación-rápida)
- [Guía de Uso](#-guía-de-uso)
- [Opciones Avanzadas](#-opciones-avanzadas)
- [Ejemplos](#-ejemplos)
- [Notas y Ética](#-notas-y-ética)

---

## ✨ Características Principales

- 🌐 **Rastreo Dinámico**: Renderiza JavaScript con **Playwright** para descubrir contenido en SPAs (Single Page Applications).
- 📡 **Intercepción de APIs**: Captura automáticamente respuestas JSON para extraer términos técnicos y datos ocultos.
- 📂 **Análisis de Metadatos**: Extrae información de archivos `.pdf` (Autor, Creador) y la convierte en parte del diccionario.
- 📧 **Extracción de OSINT**: Identifica correos electrónicos en texto, enlaces `mailto:` y respuestas de red.
- 🧠 **Procesamiento Inteligente**:
    - División de palabras compuestas (ej: `adminpanel` → `admin`, `panel`).
    - Generación de variaciones basadas en años (2024, 2025) y sufijos comunes.
    - Filtrado configurable por longitud de palabra.

---

## 🛡️ Arquitectura de Seguridad

La versión 1.1 incluye mejoras críticas:
- **Mitigación SSRF**: Validación de URLs para prevenir ataques de falsificación de peticiones del lado del servidor, bloqueando IPs locales y privadas.
- **Logging Profesional**: Sustitución de salidas estándar por un sistema de logs estructurado.
- **Validación de Esquemas**: Soporte estricto para protocolos `http` y `https`.

---

## 📦 Instalación Rápida

WWLC está optimizado para **Kali Linux** y sistemas basados en Debian.

```bash
# 1. Clonar el repositorio
git clone https://github.com/Cyberdark-Security/WWLC-Python.git
cd WWLC-Python

# 2. Configurar entorno e instalar dependencias
chmod +x setup.sh
./setup.sh

# 3. Instalar navegadores de Playwright
source venv/bin/activate
playwright install chromium
```

---

## 🛠️ Guía de Uso

Activa siempre tu entorno virtual antes de usar la herramienta:
```bash
source venv/bin/activate
./wwlc.py <URL> [opciones]
```

### Opciones Comunes:

| Argumento | Descripción |
| :--- | :--- |
| `URL` | URL objetivo (ej: `https://example.com`) |
| `-o, --output` | Archivo de salida para la wordlist (por defecto: `wordlist.txt`) |
| `-e, --email` | Activa la extracción de correos electrónicos |
| `-a, --meta` | Activa la extracción de metadatos de archivos PDF |
| `--min-length` | Longitud mínima de palabra (def: 3) |
| `--max-length` | Longitud máxima de palabra (def: 20) |

---

## 🚀 Ejemplos

**Generación básica:**
```bash
./wwlc.py https://target-app.com -o target_wordlist.txt
```

**Reconocimiento Full (Correos + Metadatos + Filtros):**
```bash
./wwlc.py https://target-app.com -e --email-file mails.txt -a --meta-file meta.txt --min-length 5
```

---

## ⚠️ Notas y Ética

- **Uso Autorizado**: Esta herramienta debe utilizarse únicamente en entornos donde se posea permiso explícito para realizar pruebas de seguridad.
- **Responsabilidad**: El equipo de desarrollo no se hace responsable del mal uso de WWLC.

---

## 🤝 Contribuciones y Contacto

¿Tienes ideas para mejorar WWLC?
1. Abre un **Issue** para discutir cambios.
2. Envía un **Pull Request** con tus mejoras.

Desarrollado por **Cyberdark Security**.
