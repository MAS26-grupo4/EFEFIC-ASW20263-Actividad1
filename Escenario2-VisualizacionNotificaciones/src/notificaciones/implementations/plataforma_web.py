#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descripción: Plataforma Web
"""

# Metadatos del módulo
__author__ = "Andrés M. Correa"
__email__ = "andrescor@unisabana.edu.co"
__status__ = "Development"  # Prototype, Development, o Production

from src.notificaciones.implementations.interfaz_plataformas import ImplementacionPlataforma

class PlataformaWeb(ImplementacionPlataforma):
    """
    Implementación de plataforma Web
    """

    def renderizar_mensaje(self, titulo: str, mensaje: str) -> None:
        print (f"🌐 [WEB] Mensaje -> {titulo}: {mensaje}")

    def renderizar_alerta(self, titulo: str, mensaje: str) -> None:
        print (f"🌐 [WEB] ⚠️ ALERTA ⚠️ -> {titulo}: {mensaje}")

    def renderizar_confirmacion(self, titulo: str, mensaje: str) -> None:
        print (f"[WEB] ✅ Confirmación -> {titulo}: {mensaje}")
