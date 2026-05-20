#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descripción: Ejecutable principal para compañía automotriz que permite
a los clientes personalizar y ordenar un automóvil de manera manual (customizado)
o usando un Director que construye a través de la Interfaz del patrón Builder,
con el que se pueden definir diferentes pre-configuraciones y consumir desde el
cliente (main) de manera simplificada

Autores: Andres M. Correa <andrescor@unisabana.edu.co>
Licencia: MIT License
"""

# Metadatos del módulo
__author__ = "Andrés M. Correa"
#__contributors__ = ["Colaborador 1 <email1@ejemplo.com>", "Colaborador 2"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Andrés M. Correa"
__email__ = "andrescor@unisabana.edu.co"
__status__ = "Production"  # Prototype, Development, o Production

from src.automotriz.core.automovil_builder_pattern import Automovil, DirectorAutomovil
import src.automotriz.core.automovil as auto

def main():
    director = DirectorAutomovil()
    automovil_base = Automovil()

    director.automovil_lujo(automovil_base)
    automovil_lujo = automovil_base.get_automovil()

    print ("--- Automovil por Director: Automovil de lujo (pre-configurado)---")
    print(automovil_lujo)

    # Construcción manual (sin director)
    automovil_base.configurar_marca(auto.MarcaAutomovil.BYD)
    automovil_base.configurar_tipo_motor(auto.TipoMotorAutomovil.ELECTRICO)
    automovil_base.configurar_sistema_sonido(auto.SistemaSonidoAutomovil.ESTANDAR)
    automovil_base.configurar_gps(True)
    automovil_custom = automovil_base.get_automovil()
    print("\n--- Automovil por Custom: Eléctrico BYD ---")
    print(automovil_custom)

if __name__ == "__main__":
    main()
