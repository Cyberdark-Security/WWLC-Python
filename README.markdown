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

WWLC v1.0 está optimizado para entornos como **Kali Linux** y otras distribuciones basadas en Debian/Ubuntu. Sigue estos pasos para instalar la herramienta.

### 1. Requisitos Previos
Asegúrate de tener instalados `git` y `pip`:
```bash
sudo apt update
sudo apt install git python3-pip -y
```

### 2. Clonar el Repositorio
Descarga el código fuente:
```bash
git clone https://github.com/Cyberdark-Security/WWLC-Python.git
cd WWLC-Python
```

### 3. Configurar el Entorno Virtual e Instalar Dependencias
Usa el script `setup.sh` para crear un entorno virtual (`venv`), instalar las dependencias listadas en `requirements.txt`, y otorgar permisos de ejecución al script principal:
```bash
chmod +x wwlc.py
chmod +x setup.sh
./setup.sh
```
> **Nota**: El script `setup.sh` instala dependencias como `beautifulsoup4`, `pypdf`, `playwright`, `requests`, entre otras. Deberías ver un mensaje como `✅ ¡Instalación completa!` al finalizar. El comando `chmod +x wwlc.py` asegura que el script sea ejecutable.

### 4. Activar el Entorno y Completar la Instalación
Activa el entorno virtual y configura los navegadores de Playwright:
```bash
source venv/bin/activate
playwright install
```
> **Importante**: El comando `playwright install` es obligatorio, ya que descarga una versión de Chromium necesaria para la automatización.

> **Nota**: Activa el entorno virtual (`source venv/bin/activate`) cada vez que abras una nueva terminal para usar WWLC.

---

## 🚀 Uso

Ejecuta WWLC con el comando:
```bash
./wwlc.py <URL> [opciones]
```

### Opciones Disponibles

| Opción | Descripción | Ejmoblo |
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

## 🛠️ Solución de Problemas

Si encuentras errores durante la instalación o ejecución, consulta las soluciones comunes a continuación:

### 1. Dependencias Faltantes de Playwright
Si al ejecutar `playwright install` ves un error como:
```
Host system is missing dependencies to run browsers.
Missing libraries: libicudata.so.66, libicui18n.so.66, libicuuc.so.66, libjpeg.so.8, libwebp.so.6, libffi.so.7
```
Instala las bibliotecas necesarias:
```bash
sudo apt install -y libicu66 libjpeg62-turbo libwebp6 libffi7
```
Luego, vuelve a ejecutar:
```bash
playwright install
```

### 2. Permiso Denegado al Ejecutar `wwlc.py`
Si ves un error como `permiso denegado: ./wwlc.py`, verifica que el script tenga permisos de ejecución:
```bash
chmod +x wwlc.py
```
Asegúrate de estar en el entorno virtual (`source venv/bin/activate`) y prueba de nuevo:
```bash
./wwlc.py --help
```

### 3. Otros Errores
- **Entorno virtual no activado**: Asegúrate de activar el entorno con `source venv/bin/activate` antes de ejecutar `playwright install` o `wwlc.py`.
- **Dependencias no instaladas**: Si `setup.sh` falla, verifica que `requirements.txt` esté presente y ejecuta manualmente:
  ```bash
  pip install -r requirements.txt
  ```
- Para más ayuda, crea un *issue* en el [repositorio de GitHub](https://github.com/Cyberdark-Security/WWLC-Python).

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