# -*- coding: utf-8 -*-

class Automovil:
    """El objeto complejo que contiene todas las configuraciones."""
    def __init__(self):
        self.motor = "Estándar"
        self.color = "Blanco"
        self.llantas = "Rines 16"
        self.sistema_sonido = "Básico"
        self.interiores = "Cuero"
        self.techo_solar = False
        self.gps = False

    def __str__(self):
        return (f"Auto [Motor: {self.motor}, Color: {self.color}, "
                f"Llantas: {self.llantas}, Sonido: {self.sistema_sonido}, "
                f"Interiores: {self.interiores}, Techo Solar: {self.techo_solar}, "
                f"GPS: {self.gps}]")


class AutomovilBuilder:
    """El Constructor que maneja la configuración paso a paso."""
    def __init__(self):
        self._automovil = Automovil()

    def set_motor(self, tipo: str):
        self._automovil.motor = tipo
        return self

    def set_color(self, color: str):
        self._automovil.color = color
        return self

    def set_llantas(self, tipo: str):
        self._automovil.llantas = tipo
        return self

    def set_sistema_sonido(self, tipo: str):
        self._automovil.sistema_sonido = tipo
        return self

    def set_interiores(self, tipo: str):
        self._automovil.interiores = tipo
        return self

    def con_techo_solar(self):
        self._automovil.techo_solar = True
        return self

    def con_gps(self):
        self._automovil.gps = True
        return self

    def build(self) -> Automovil:
        """Retorna el objeto final completamente configurado."""
        return self._automovil
