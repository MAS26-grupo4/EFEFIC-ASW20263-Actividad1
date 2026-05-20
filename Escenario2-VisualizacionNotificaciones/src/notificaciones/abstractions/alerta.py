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

class NotificacionAlerta(AbstraccionNotificaciones):
    def enviar(self, titulo: str, contenido: str) -> None:
        """
        Notificación de Alerta
        """
        self._plataforma.renderizar_alerta(titulo, contenido)