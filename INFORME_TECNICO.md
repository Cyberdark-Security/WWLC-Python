# Informe Técnico de WWLC (Web Wordlist Creator)

## 1. Arquitectura del Repositorio

El repositorio contiene una herramienta de seguridad diseñada para el reconocimiento y la generación de diccionarios (wordlists) personalizados a partir de activos web.

### Componentes Principales:
- **`wwlc.py`**: El núcleo de la herramienta. Gestiona el rastreo, la intercepción de tráfico y el procesamiento de datos.
- **`setup.sh`**: Script de automatización para la configuración del entorno virtual y la instalación de dependencias.
- **`requirements.txt`**: Listado de librerías de Python necesarias para el funcionamiento.
- **`README.markdown`**: Documentación inicial del proyecto.

---

## 2. Análisis Técnico de `wwlc.py`

### Flujo de Ejecución:
1. **Inicialización**: Se procesan los argumentos de línea de comandos mediante `argparse`.
2. **Configuración de Red**: Se establece una sesión de `requests` con un User-Agent personalizado y se inicializa `playwright`.
3. **Rastreo Dinámico**:
   - Utiliza un navegador Chromium (vía Playwright) para cargar las páginas. Esto permite ejecutar JavaScript y descubrir contenido que los scrapers estáticos ignoran.
   - **Intercepción de APIs**: Se monitorean las respuestas de la red. Si se detecta una respuesta `application/json`, el contenido se captura para su posterior extracción de palabras.
4. **Procesamiento de Contenido**:
   - **HTML**: `BeautifulSoup` elimina etiquetas de script y estilo, extrayendo el texto visible.
   - **Documentos**: Los enlaces a archivos `.pdf` se descargan y analizan con `pypdf` para extraer metadatos (Autor, Creador).
5. **Generación de Wordlist**:
   - Limpieza y tokenización de texto.
   - División de palabras compuestas.
   - Generación de variaciones comunes (sufijos, años, etc.).
6. **Salida**: Los resultados se guardan en archivos de texto según las opciones seleccionadas.

### Librerías Críticas:
- **`playwright`**: Fundamental para aplicaciones web modernas (SPAs).
- **`beautifulsoup4`**: Extracción eficiente de texto de estructuras HTML.
- **`pypdf`**: Análisis de documentos binarios.
- **`requests`**: Manejo de descargas fuera del contexto del navegador.

---

## 3. Evaluación de Seguridad y Desarrollo

### Fortalezas:
- Capacidad de lidiar con contenido dinámico.
- Extracción multicanal (HTML, API, Metadatos).

### Debilidades y Riesgos Identificados:
- **SSRF (Server-Side Request Forgery)**: El script no valida si las URLs a visitar o descargar pertenecen a rangos de IP privados o locales (ej. `localhost`, `169.254.169.254`). Un atacante podría usar la herramienta para escanear redes internas desde la máquina donde se ejecuta.
- **Manejo de Errores**: Aunque existen bloques `try-except`, la gestión de excepciones es genérica y los mensajes se envían principalmente a `stdout/stderr` mediante `print`.
- **Modularidad**: La lógica principal está concentrada en la función `main()`, lo que dificulta las pruebas unitarias y la escalabilidad.
- **Validación de Entradas**: Falta de saneamiento riguroso en las URLs de entrada.

---

## 4. Propuesta de Mejoras

### Seguridad:
- **Validación de URLs**: Implementar una lista negra de rangos de IP y validación de esquemas (solo `http` y `https`).
- **User-Agent Aleatorio**: Para evitar el bloqueo por parte de WAFs.

### Desarrollo:
- **Logging**: Migrar de `print` a la librería `logging` de Python para un control granular de la verbosidad.
- **Refactorización**: Separar el rastreador, el procesador de documentos y el generador de variaciones en clases o módulos independientes.
- **Tipado Estático**: Añadir Type Hints para mejorar la legibilidad y detectar errores en tiempo de desarrollo.
- **Tests**: Implementar pruebas unitarias para las funciones de procesamiento de palabras.
