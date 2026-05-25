from __future__ import annotations
from src.chats.interfaz_chat_mediador import ChatMediador
from usuarios.usuario_abstracto import UsuarioAbstracto

class ChatTextoMediador(ChatMediador):
    def __init__(self):
        self._usuarios: dict[str, UsuarioAbstracto] = {}
        self._grupos: dict[str, list[str]] = {}

    def registrar_usuario(self, usuario: UsuarioAbstracto) -> None:
        if usuario.id_usuario not in self._usuarios:
            self._usuarios[usuario.id_usuario] = usuario
            print(f"El usuario: {usuario.nombre} ha sido registrado con el id: {usuario.id_usuario}")

    def crear_grupo(self, id_grupo: str, ids_usuarios: list[str]) -> None:
        self._grupos[id_grupo] = ids_usuarios

    def enviar_mensaje_privado(self, id_emisor: str, id_receptor: str, mensaje: str) -> None:
        receptor = self._usuarios.get(id_receptor)
        emisor = self._usuarios.get(id_emisor)
        if receptor and emisor:
            receptor.recibir_mensaje(id_emisor, emisor.nombre, mensaje, es_grupal=False)
        else:
            print(f"⚠️ Error: Usuario {id_receptor} no encontrado.")

    def enviar_mensaje_grupal(self, id_emisor: str, id_grupo: str, mensaje: str) -> None:

        emisor = self._usuarios.get(id_emisor)
        miembros_grupo = self._grupos.get(id_grupo)

        if not miembros_grupo:
            print(f"⚠️ Error: Grupo {id_grupo} no existe.")
            return

        for id_usuario in miembros_grupo:
            if id_usuario != id_emisor:
                usuario = self._usuarios.get(id_usuario)
                if usuario and emisor:
                    usuario.recibir_mensaje(id_emisor, emisor.nombre, mensaje, es_grupal=True)
