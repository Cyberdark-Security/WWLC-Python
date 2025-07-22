#!/bin/bash

echo "--- Creando entorno virtual en la carpeta 'venv' ---"
python3 -m venv venv

echo "--- Activando entorno e instalando dependencias desde requirements.txt ---"
# Activa el entorno y luego instala los paquetes
source venv/bin/activate
pip install -r requirements.txt

echo ""
echo "✅ ¡Instalación completa!"
echo ""
echo "Para usar la herramienta, primero activa el entorno con el comando:"
echo "source venv/bin/activate"
echo ""
echo "Y luego ejecuta el script, por ejemplo:"
echo "./wwlc.py --help"