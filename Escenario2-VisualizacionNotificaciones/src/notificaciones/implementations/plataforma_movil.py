#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descripción: Plataforma Móvil
"""

# Metadatos del módulo
__author__ = "Andrés M. Correa"
__email__ = "andrescor@unisabana.edu.co"
__status__ = "Development"  # Prototype, Development, o Production

from src.notificaciones.implementations.interfaz_plataformas import ImplementacionPlataforma

class PlataformaMovil(ImplementacionPlataforma):
    """
    Implementación de Plataforma Móvil
    """

    def renderizar_mensaje(self, titulo: str, mensaje: str) -> None:
        print (f"📱 [MÓVIL] Mensaje -> {titulo}: {mensaje}")

    def renderizar_alerta(self, titulo: str, mensaje: str) -> None:
        print (f"📱 [MÓVIL] ⚠️ ALERTA ⚠️ -> {titulo}: {mensaje}")

    def renderizar_confirmacion(self, titulo: str, mensaje: str) -> None:
        print (f"📱 [MÓVIL] ✅ Confirmación -> {titulo}: {mensaje}")