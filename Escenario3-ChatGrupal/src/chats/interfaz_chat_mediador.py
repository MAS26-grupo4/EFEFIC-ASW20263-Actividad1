from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Requiere TYPE_CHECKING para el usuario abstracto dada la referencia circular entre archivos
if TYPE_CHECKING:
    from src.usuarios.usuario_abstracto import UsuarioAbstracto

class ChatMediador(ABC):
    """
    Interfaz del mediador para la comunicación de mensajes de chat
    """

    @abstractmethod
    def registrar_usuario(self, usuario: UsuarioAbstracto):
        pass

    @abstractmethod
    def enviar_mensaje_privado(self, id_emisor: str, id_receptor: str, mensaje: str):
        pass

    @abstractmethod
    def enviar_mensaje_grupal(self, id_emisor: str, id_grupo: str, mensaje: str):
        pass

