#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descripción: Objeto Automóvil
"""

# Metadatos del módulo
__author__ = "Andrés M. Correa"
__email__ = "andrescor@unisabana.edu.co"
__status__ = "Production"  # Prototype, Development, o Production

from enum import StrEnum

class MarcaAutomovil(StrEnum):
    RENAULT = "RENAULT"
    CHEVROLET = "CHEVROLET"
    TOYOTA = "TOYOTA"
    BYD = "BYD"

class TipoMotorAutomovil(StrEnum):
    GASOLINA = "Gasolina"
    DIESEL = "Diesel"
    ELECTRICO = "Eléctrico"
    HIBRIDO = "Híbrido"

class ColorAutomovil(StrEnum):
    ROJO = "Rojo"
    AZUL = "Azul"
    BLANCO = "Blanco"
    GRIS = "Gris"
    NEGRO = "Negro"

class TipoLlantasAutomovil(StrEnum):
    TODA_TEMPORADA = "Toda Temporada"
    VERANO = "Verano"
    INVIERNO = "Invierno"

class SistemaSonidoAutomovil(StrEnum):
    ESTANDAR = "Estándar"
    PREMIUM = "Premium"

class InterioresAutomovil(StrEnum):
    ESTANDAR = "Estándar"
    CUERO = "Cuero"
    LUJO = "Lujo"

class ObjetoAutomovil:
    def __init__(self):
        self.marca = MarcaAutomovil(MarcaAutomovil.CHEVROLET)
        self.tipo_motor = TipoMotorAutomovil(TipoMotorAutomovil.GASOLINA)
        self.color = ColorAutomovil(ColorAutomovil.GRIS)
        self.tipo_llantas = TipoLlantasAutomovil(TipoLlantasAutomovil.TODA_TEMPORADA)
        self.sistema_sonido = SistemaSonidoAutomovil(SistemaSonidoAutomovil.ESTANDAR)
        self.interiores = InterioresAutomovil(InterioresAutomovil.ESTANDAR)
        self.techo_solar = False
        self.gps = False


    def __str__(self) -> str:
#        return str(self.__dict__)
        return (f"Auto [Marca: {self.marca}, Motor: {self.tipo_motor}, "
                f"Color: {self.color}, "
                f"Llantas: {self.tipo_llantas}, Sonido: {self.sistema_sonido}, "
                f"Interiores: {self.interiores}, Techo Solar: {self.techo_solar}, "
                f"GPS: {self.gps}]")