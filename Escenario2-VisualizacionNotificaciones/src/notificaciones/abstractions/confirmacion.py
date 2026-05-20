#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descripción: Notificación Mensaje
"""

# Metadatos del módulo
__author__ = "Andrés M. Correa"
__email__ = "andrescor@unisabana.edu.co"
__status__ = "Development"  # Prototype, Development, o Production

from src.notificaciones.abstractions.abstract_notifications import AbstraccionNotificaciones

class NotificacionConfirmacion(AbstraccionNotificaciones):
    """
    Notificación de Confirmación
    """

    def enviar(self, titulo: str, contenido: str) -> None:
        self._plataforma.renderizar_confirmacion(titulo, contenido)