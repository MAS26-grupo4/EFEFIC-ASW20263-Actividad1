from __future__ import annotations
from abc import ABC, abstractmethod
from automotriz.core.automovil import *

class InterfazAutomovil(ABC):
    """
    Interface de Automovil que especifica los métodos para crear diferentes
    partes del objeto Automovil
    """

    @property
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def configurar_marca(self, marca: MarcaAutomovil) -> None:
        pass

    @abstractmethod
    def configurar_tipo_motor(self, motor: TipoMotorAutomovil) -> None:
        pass

    @abstractmethod
    def configurar_color(self, color: ColorAutomovil) -> None:
        pass

    @abstractmethod
    def configurar_tipo_llantas(self, llantas: TipoLlantasAutomovil) -> None:
        pass

    @abstractmethod
    def configurar_sistema_sonido(self, sistema_sonido: SistemaSonidoAutomovil) -> None:
        pass

    @abstractmethod
    def configurar_interiores(self, interiores: InterioresAutomovil) -> None:
        pass

    @abstractmethod
    def configurar_techo_solar(self, techo_solar: bool) -> None:
        pass

    @abstractmethod
    def configurar_gps(self, gps: bool) -> None:
        pass

class Automovil(InterfazAutomovil):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._automovil = ObjetoAutomovil()

    def configurar_marca(self, marca: MarcaAutomovil) -> None:
        self._automovil.marca = marca

    def configurar_tipo_motor(self, motor: TipoMotorAutomovil) -> None:
        self._automovil.tipo_motor = motor

    def configurar_color(self, color: ColorAutomovil) -> None:
        self._automovil.color = color

    def configurar_tipo_llantas(self, llantas: TipoLlantasAutomovil) -> None:
        self._automovil.tipo_llantas = llantas

    def configurar_sistema_sonido(self, sistema_sonido: SistemaSonidoAutomovil) -> None:
        self._automovil.sistema_sonido = sistema_sonido

    def configurar_interiores(self, interiores: InterioresAutomovil) -> None:
        self._automovil.interiores = interiores

    def configurar_techo_solar(self, techo_solar: bool) -> None:
        self._automovil.techo_solar = techo_solar

    def configurar_gps(self, gps: bool) -> None:
        self._automovil.gps = gps

    def get_automovil(self) -> Automovil:
        producto = self._automovil
        self.reset()
        return producto

class DirectorAutomovil:
    def automovil_lujo(self, interfaz: InterfazAutomovil) -> None:
        interfaz.reset()
        interfaz.configurar_marca(MarcaAutomovil.TOYOTA)
        interfaz.configurar_tipo_motor(TipoMotorAutomovil.ELECTRICO)
        interfaz.configurar_interiores(InterioresAutomovil.LUJO)
        interfaz.configurar_sistema_sonido(SistemaSonidoAutomovil.PREMIUM)
        interfaz.configurar_techo_solar(True)
        interfaz.configurar_gps(True)