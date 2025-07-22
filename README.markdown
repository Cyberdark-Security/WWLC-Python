# 🐍 WWLC - Web Wordlist Creator (v1.0)

**WWLC (Web Wordlist Creator)** es una herramienta avanzada escrita en **Python** para generar diccionarios de palabras personalizados a partir de sitios web. Diseñada para tareas de reconocimiento, WWLC destaca por su capacidad de extraer contenido dinámico y datos ocultos, superando las limitaciones de los scrapers tradicionales.

---

## 🌟 Características Principales

- **Análisis Dinámico**: Utiliza **Playwright** para renderizar JavaScript y extraer contenido de aplicaciones web modernas.
- **Intercepción de APIs**: Captura respuestas de APIs en formato JSON para descubrir datos adicionales.
- **Rastreo Profundo**: Navega automáticamente por enlaces del mismo dominio para recopilar más contenido.
- **Extracción de Correos**: Identifica direcciones de correo en texto, enlaces `mailto:` y respuestas de APIs.
- **Análisis de Metadatos**: Descarga y extrae metadatos de archivos `.pdf`, como autor y creador.
- **Procesamiento Inteligente de Palabras**:
  - Limpieza y formateo automático de palabras.
  - Filtrado de fechas, horas y términos numéricos.
  - División de palabras compuestas (ej: "websecurity" → "web", "security").
  - Generación de variaciones comunes para contraseñas.

---

## 🛠️ Instalación

WWLC v1.0 está optimizado para entornos como **Kali Linux** y otras distribuciones basadas en Debian/Ubuntu.

### Requisitos Previos
Asegúrate de tener instalados `git` y `pip`:
```bash
sudo apt update
sudo apt install git python3-pip -y
```

### Pasos de Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Cyberdark-Security/WWLC-Python.git
   cd WWLC-Python
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura los navegadores de Playwright:
   ```bash
   playwright install
   ```

> **Nota**: El comando `playwright install` descarga una versión de Chromium necesaria para la automatización.

---

## 🚀 Uso

Ejecuta WWLC con el comando:
```bash
./wwlc.py <URL> [opciones]
```

### Opciones Disponibles

| Opción | Descripción | Ejemplo |
|--------|-------------|---------|
| `URL` | **Requerido**. URL del sitio web a analizar. | `./wwlc.py https://example.com` |
| `-o, --output <archivo>` | Especifica el archivo de salida para la lista de palabras (por defecto: `wordlist.txt`). | `./wwlc.py https://example.com -o mi_diccionario.txt` |
| `-e, --email` | Activa la extracción de correos electrónicos. | `./wwlc.py https://example.com -e` |
| `--email-file <archivo>` | Guarda los correos en un archivo específico (requiere `-e`). | `./wwlc.py https://example.com -e --email-file correos.txt` |
| `-a, --meta` | Activa la extracción de metadatos de archivos `.pdf`. | `./wwlc.py https://example.com -a` |
| `--meta-file <archivo>` | Guarda las palabras de metadatos en un archivo (requiere `-a`). | `./wwlc.py https://example.com -a --meta-file meta.txt` |
| `--min-length <número>` | Filtra palabras por longitud mínima (por defecto: 3). | `./wwlc.py https://example.com --min-length 5` |
| `--max-length <número>` | Filtra palabras por longitud máxima (por defecto: 20). | `./wwlc.py https://example.com --max-length 10` |
| `--no-split` | Desactiva la división de palabras compuestas. | `./wwlc.py https://example.com --no-split` |
| `--no-variations` | Desactiva la generación de variaciones de palabras. | `./wwlc.py https://example.com --no-variations` |
| `--help` | Muestra el menú de ayuda. | `./wwlc.py --help` |

---

## 📋 Ejemplo Completo

Para analizar un sitio, extraer correos, metadatos y generar una lista de palabras con longitud mínima de 5 caracteres:
```bash
./wwlc.py https://example.com -e --email-file correos.txt -a --meta-file meta.txt --min-length 5 -o palabras.txt
```

---

## ⚠️ Notas Importantes

- **Uso Ético**: WWLC v1.0 está diseñado para pruebas de seguridad autorizadas. Úsalo solo en sitios web donde tengas permiso explícito.
- **Rendimiento**: El rastreo profundo y la extracción de APIs pueden consumir tiempo y recursos en sitios grandes.
- **Soporte de Archivos**: Actualmente, la extracción de metadatos está limitada a archivos `.pdf`.

---

## 📜 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles.

---

## 🤝 Contribuciones

¡Contribuye al proyecto! Si tienes ideas, mejoras o encuentras errores:
1. Crea un *issue* en el repositorio.
2. Envía un *pull request* con tus cambios.

---

## 📬 Contacto

Para soporte o consultas, contacta al equipo de **Cyberdark Security** a través de nuestro [repositorio en GitHub](https://github.com/Cyberdark-Security/WWLC-Python).