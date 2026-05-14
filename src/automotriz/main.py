#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nombre del Módulo: Principal (main.py)
Descripción: Ejecutable principal para compañía automotriz que permite
a los clientes personalizar y ordenar un automóvil

Autores: Andres M. Correa <andrescor@unisabana.edu.co>
Licencia: MIT License (o la licencia que aplique)
"""

# Metadatos del módulo
__author__ = "Andrés M. Correa"
__contributors__ = ["Colaborador 1 <email1@ejemplo.com>", "Colaborador 2"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Andrés M. Correa"
__email__ = "andrescor@unisabana.edu.co"
__status__ = "Development"  # Prototype, Development, o Production

from automovilBuilder import AutomovilBuilder

def main():
    auto_deportivo = (AutomovilBuilder()
                      .set_motor("V8 Turbo")
                      .set_color("Rojo")
                      .set_llantas("Rines 19 Deportivos")
                      .set_sistema_sonido("Bose")
                      .set_interiores("Cuero")
                      .con_techo_solar()
                      .con_gps()
                      .build())

    auto_economico = (AutomovilBuilder()
                      .set_color("Gris")
                      .build())

    print(auto_deportivo)
    print(auto_economico)

if __name__ == "__main__":
    main()
