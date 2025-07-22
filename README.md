# 🐍 WWLC - Web Wordlist Creator

**WWLC (Web Wordlist Creator)** es una potente herramienta de reconocimiento escrita en Python, diseñada para generar diccionarios de palabras altamente personalizados a partir de sitios web.

A diferencia de otros scrapers, WWLC utiliza un navegador automatizado para analizar no solo el contenido HTML visible, sino también los datos cargados dinámicamente a través de APIs. Esto permite descubrir palabras, correos electrónicos y metadatos que estarían ocultos para herramientas más simples.

---

## ✨ Características Principales

* **Análisis Dinámico**: Utiliza Playwright para renderizar JavaScript, permitiendo extraer contenido de aplicaciones web modernas.
* **Intercepción de APIs**: Captura y analiza las respuestas de las peticiones a APIs (en formato JSON) para encontrar datos adicionales.
* **Rastreo en Profundidad**: Navega por los enlaces de la página para descubrir más contenido dentro del mismo dominio.
* **Extracción de Correos**: Recopila direcciones de correo electrónico tanto del texto visible como de los enlaces `mailto:`.
* **Extracción de Metadatos**: Descarga y analiza archivos `.pdf` para extraer metadatos valiosos, como nombres de autor y creador.
* **Procesamiento Avanzado de Palabras**:
    * Limpia y formatea las palabras extraídas.
    * Filtra fechas, horas y palabras puramente numéricas.
    * Divide palabras compuestas (ej: "websecurity" -> "web", "security").
    * Genera variaciones comunes para contraseñas.

---

## ⚙️ Instalación en Kali Linux (y otros Debian/Ubuntu)

El script está diseñado para funcionar sin problemas en un entorno como Kali.

#### 1. Prerrequisitos
Asegúrate de tener `git` y `pip` instalados. Kali Linux generalmente los incluye por defecto.
```bash
sudo apt update
sudo apt install git python3-pip -y
```

#### 2. Instalación de WWLC
Sigue estos pasos en tu terminal:

```bash
# Clona el repositorio desde GitHub
git clone [https://github.com/Cyberdark-Security/WWLC-Python.git](https://github.com/Cyberdark-Security/WWLC-Python.git)

# Entra en la carpeta del proyecto
cd WWLC-Python

# Instala las dependencias de Python (Playwright, BeautifulSoup, etc.)
pip install -r requirements.txt

# Instala los navegadores que Playwright necesita (¡Paso crucial!)
# Este comando descarga una versión de Chromium para la automatización.
playwright install
```

---

## 🚀 Uso

La estructura básica del comando es: ` ./wwlc.py <URL> [opciones]`

### Desglose de Opciones (Flags)

* `URL` (Requerido)
    _El único argumento obligatorio. Es la dirección del sitio web que quieres analizar._
    ```bash
    ./wwlc.py [https://ejemplo.com](https://ejemplo.com)
    ```

* `-o, --output <archivo>`
    _Guarda la lista de palabras principal en el archivo especificado. Si no se usa, el script creará un archivo `wordlist.txt` por defecto._
    ```bash
    ./wwlc.py [https://ejemplo.com](https://ejemplo.com) -o mi_diccionario.txt
    ```

* `-e, --email`
    _Activa la extracción de correos electrónicos. El script buscará correos en el texto, en los enlaces `mailto:` y en las respuestas de las APIs._
    ```bash
    ./wwlc.py [https://ejemplo.com](https://ejemplo.com) -e --email-file correos.txt
    ```

* `--email-file <archivo>`
    _Especifica el archivo donde se guardarán los correos encontrados. **Requiere que el flag `-e` esté activado**._
    ```bash
    ./wwlc.py [https://ejemplo.com](https://ejemplo.com) -e --email-file emails_encontrados.txt
    ```

* `-a, --meta`
    _Activa la extracción de metadatos de documentos (actualmente soporta `.pdf`). El script descargará los archivos y buscará información como el autor._
    ```bash
    ./wwlc.py [https://sitio-con-pdfs.com](https://sitio-con-pdfs.com) -a --meta-file usuarios.txt
    ```

* `--meta-file <archivo>`
    _Especifica el archivo donde se guardarán las palabras extraídas de los metadatos. **Requiere que el flag `-a` esté activado**._
    ```bash
    ./wwlc.py [https://sitio-con-pdfs.com](https://sitio-con-pdfs.com) -a --meta-file meta_palabras.txt
    ```

* `--min-length <número>`
    _Filtra la lista de palabras final para incluir solo aquellas con una longitud mínima. El valor por defecto es 3._
    ```bash
    ./wwlc.py [https://ejemplo.com](https://ejemplo.com) --min-length 5
    ```

* `--max-length <número>`
    _Filtra la lista de palabras final para incluir solo aquellas con una longitud máxima. El valor por defecto es 20._
    ```bash
    ./wwlc.py [https://ejemplo.com](https://ejemplo.com) --max-length 10
    ```

* `--no-split`
    _Desactiva la función de dividir palabras compuestas (ej: "passwordseguro" no se dividirá en "password" y "seguro")._
    ```bash
    ./wwlc.py [https://ejemplo.com](https://ejemplo.com) --no-split
    ```

* `--no-variations`
    _Desactiva la generación de variaciones simples (ej: a "palabra" no se le añadirán números como "palabra2025")._
    ```bash
    ./wwlc.py [https://ejemplo.com](https://ejemplo.com) --no-variations
    ```

* `--help`
    _Muestra el menú de ayuda con todas las opciones disponibles._
    ```bash
    ./wwlc.py --help
    ```
---

##