from abc import ABC, abstractmethod
from src.chats.interfaz_chat_mediador import ChatMediador

class UsuarioAbstracto(ABC):
    def __init__(self, mediador: ChatMediador, id_usuario: str, nombre: str):
        self.mediador = mediador
        self.id_usuario: str = id_usuario
        self.nombre: str = nombre

    @abstractmethod
    def enviar_mensaje_privado(self, id_receptor: str, mensaje: str ):
        pass

    @abstractmethod
    def enviar_mensaje_grupal(self, id_grupo: str, mensaje: str ):
        pass

    @abstractmethod
    def recibir_mensaje(self, id_emisor: str, nombre_emisor: str, mensaje: str, es_grupal: bool):
        pass