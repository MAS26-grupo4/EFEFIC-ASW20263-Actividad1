#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descripción: Abstracción para las notificaciones
"""

# Metadatos del módulo
__author__ = "Andrés M. Correa"
__email__ = "andrescor@unisabana.edu.co"
__status__ = "Development"  # Prototype, Development, o Production

from abc import ABC, abstractmethod
from src.notificaciones.implementations.interfaz_plataformas import ImplementacionPlataforma

class AbstraccionNotificaciones(ABC):
    """
    Abstracción para las notificaciones
    """

    def __init__(self, plataforma: ImplementacionPlataforma) -> None:
        self._plataforma = plataforma

    @abstractmethod
    def enviar(self, titulo: str, contenido: str) -> str:
        pass