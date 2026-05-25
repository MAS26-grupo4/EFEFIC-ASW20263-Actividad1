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
from src.notificaciones.implementations.plataforma_movil import PlataformaMovil


def main():
    canal_web = PlataformaWeb()
    alerta = NotificacionAlerta(canal_web)
    mensaje = NotificacionMensaje(canal_web)
    confirmacion = NotificacionConfirmacion(canal_web)

    print("----- Notificaciones Web -----")
    alerta.enviar("Alerta de Seguridad", "Fallo de origen.")
    mensaje.enviar("Mensaje", "Próxima notificación en 10 mins")
    confirmacion.enviar("Confirmación", "Confirmación OK")

    canal_movil = PlataformaMovil()
    alerta_movil = NotificacionAlerta(canal_movil)
    confirmacion_movil = NotificacionConfirmacion(canal_movil)

    print("\n\n----- Notificaciones Móviles -----")
    alerta_movil.enviar("Alerta de batería", "Batería baja.")
    confirmacion_movil.enviar("Confirmación", "Confirmación OK")

if __name__ == "__main__":
    main()

