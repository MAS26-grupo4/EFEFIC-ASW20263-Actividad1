#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descripción: Interfaz para la implementación de las plataformas
"""

# Metadatos del módulo
__author__ = "Andrés M. Correa"
__email__ = "andrescor@unisabana.edu.co"
__status__ = "Developement"  # Prototype, Development, o Production

from abc import ABC, abstractmethod

class ImplementacionPlataforma(ABC):
    """
    Implementación de las plataformas a través de una interfaz
    """
    @abstractmethod
    def renderizar_mensaje(self, titulo: str, mensaje: str) -> str:
        pass

    @abstractmethod
    def renderizar_alerta(self, titulo: str, mensaje: str) -> str:
        pass

    @abstractmethod
    def renderizar_confirmacion(self, titulo: str, mensaje: str) -> str:
        pass
