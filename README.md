# WWLC - Web Wordlist Creator 🐍

WWLC es una herramienta sencilla escrita en Python para generar diccionarios de palabras personalizadas (wordlists) a partir del contenido de un sitio web. Extrae palabras únicas y las prepara para ser usadas en auditorías de seguridad.

## Características
- Extrae todas las palabras de una URL.
- Limpia y formatea las palabras.
- Divide palabras compuestas (ej: "websecurity" -> "web", "security").
- Genera variaciones comunes para contraseñas.

## Instalación en Kali Linux (y otros Linux)

El proceso es muy sencillo y rápido.

```bash
# 1. Clona el repositorio desde GitHub
git clone [https://github.com/tu-usuario/WWLC-Python.git](https://github.com/tu-usuario/WWLC-Python.git)

# 2. Entra en la carpeta del proyecto
cd WWLC-Python

# 3. Instala las dependencias necesarias con pip
pip install -r requirements.txt
```

## Uso

Una vez instalado, puedes ejecutar la herramienta de la siguiente manera:

**Ejemplo básico (muestra la lista en la terminal):**
```bash
./wwlc.py [https://ejemplo.com](https://ejemplo.com)
```

**Ejemplo guardando la lista en un archivo:**
```bash
./wwlc.py [https://ejemplo.com](https://ejemplo.com) -o mi_wordlist.txt
```
**Para ver todas las opciones disponibles:**
```bash
./wwlc.py --help
```

## Licencia
Este proyecto está bajo la Licencia MIT.