#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descripción: Interfaz para la implementación de las plataformas
"""

# Metadatos del módulo
__author__ = "Andrés M. Correa"
__email__ = "andrescor@unisabana.edu.co"
__status__ = "Developement"  # Prototype, Development, o Production

from notificaciones.abstractions.alerta import NotificacionAlerta
from notificaciones.abstractions.mensaje import NotificacionMensaje
from notificaciones.abstractions.confirmacion import NotificacionConfirmacion
from src.notificaciones.implementations.plataforma_web import PlataformaWeb

if __name__ == "__main__":
    canal_web = PlataformaWeb()
    alerta = NotificacionAlerta(canal_web)
    mensaje = NotificacionMensaje(canal_web)
    confirmacion = NotificacionConfirmacion(canal_web)

    alerta.enviar("Alerta de Seguridad", "Fallo de origen.")
    mensaje.enviar("Mensaje", "Próxima notificación en 10 mins")
    confirmacion.enviar("Confirmación", "Confirmación OK")
