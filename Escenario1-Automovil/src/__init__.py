import os
import sys

# Detecta automáticamente la ubicación de la carpeta 'src'
_src_path = os.path.dirname(os.path.abspath(__file__))

# Le dice a Python que busque los paquetes aquí adentro
if _src_path not in sys.path:
    sys.path.insert(0, _src_path)
