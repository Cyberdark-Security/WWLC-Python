# 🚀 WWLC - Web Wordlist Creator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

**WWLC (Web Wordlist Creator)** es una potente herramienta de reconocimiento diseñada para la generación automatizada de diccionarios (wordlists) altamente personalizados. Su propósito es facilitar la recolección de terminología, rutas y datos específicos de activos web para su uso en auditorías de seguridad y pruebas de penetración.

A diferencia de los scrapers estáticos, WWLC emplea automatización de navegador para interactuar con aplicaciones modernas y capturar datos que residen en el DOM dinámico y el tráfico de red.

---

## 📋 Tabla de Contenidos
- [Funcionalidades Principales](#-funcionalidades-principales)
- [¿Por qué usar WWLC?](#-por-qué-usar-wwlc)
- [Instalación](#-instalación)
- [Guía de Uso](#-guía-de-uso)
- [Opciones de Configuración](#-opciones-de-configuración)
- [Ejemplos de Aplicación](#-ejemplos-de-aplicación)

---

## ✨ Funcionalidades Principales

- 🌐 **Navegación Dinámica**: Renderiza JavaScript mediante **Playwright**, permitiendo analizar SPAs y sitios con carga diferida.
- 📡 **Extracción de Tráfico de Red**: Intercepta respuestas de APIs (JSON) para capturar endpoints, parámetros y datos técnicos ocultos.
- 📂 **Análisis de Documentos**: Descarga y extrae metadatos de archivos PDF para identificar nombres de autores, software de creación y otros términos clave.
- 📧 **OSINT integrado**: Identifica automáticamente direcciones de correo electrónico en el contenido visual y en el código fuente.
- 🧠 **Motor de Procesamiento**:
    - Limpieza inteligente de ruido y filtrado por longitud.
    - División de palabras compuestas para maximizar la cobertura del diccionario.
    - Generación de variaciones predictivas (sufijos numéricos, años actuales).

---

## 🛠️ ¿Por qué usar WWLC?

En escenarios de seguridad, un diccionario genérico suele ser insuficiente. WWLC permite construir una wordlist **específica al contexto** del objetivo, aumentando drásticamente la efectividad en ataques de fuerza bruta, descubrimiento de directorios y pruebas de contraseñas.

---

## 📦 Instalación

Optimizado para entornos de seguridad como **Kali Linux**.

```bash
# 1. Clonar el repositorio
git clone https://github.com/Cyberdark-Security/WWLC-Python.git
cd WWLC-Python

# 2. Configurar el entorno
chmod +x setup.sh
./setup.sh

# 3. Preparar el motor de navegación
source venv/bin/activate
playwright install chromium
```

---

## 🚀 Guía de Uso

Asegúrese de activar el entorno virtual antes de cada sesión:

```bash
source venv/bin/activate
./wwlc.py <URL> [opciones]
```

### Opciones de Configuración:

| Icono | Argumento | Descripción |
| :---: | :--- | :--- |
| 🎯 | `URL` | Objetivo principal a analizar |
| 💾 | `-o, --output` | Nombre del archivo de salida |
| ✉️ | `-e, --email` | Habilitar extracción de correos |
| 📑 | `-a, --meta` | Procesar metadatos de documentos PDF |
| 📏 | `--min-length` | Definir longitud mínima de palabras |

---

## 💡 Ejemplos de Aplicación

**Generación de diccionario enfocado en APIs:**
```bash
./wwlc.py https://api.target.com -o api_keys.txt
```

**Reconocimiento profundo con metadatos y OSINT:**
```bash
./wwlc.py https://target.com -e --email-file mails.txt -a --meta-file pdf_meta.txt
```

---

**Hecho por Cyberdark by Whoami-labs.com**
