from src.usuarios.usuario_abstracto import UsuarioAbstracto

class ChatUsuario(UsuarioAbstracto):
    """
    Implementación de un mensaje chat de usuario
    """

    def enviar_mensaje_privado(self, id_receptor: str, mensaje: str ) -> None:
        """
        Método para enviar mensaje privado

        id_receptor: id de quien recibe el mensaje de chat
        mensaje:  mensaje de usuario
        """
        _id_emisor = self.id_usuario
        self.mediador.enviar_mensaje_privado(_id_emisor, id_receptor, mensaje)

    def enviar_mensaje_grupal(self, id_grupo: str, mensaje: str ) -> None:
        """
        Método para enviar mensaje grupal

        id_grupo: id del grupo que debe recibir el mensaje de chat
        mensaje:  mensaje de usuario
        """
        _id_emisor = self.id_usuario
        self.mediador.enviar_mensaje_grupal(_id_emisor, id_grupo, mensaje)

    def recibir_mensaje(self, id_emisor: str, nombre_emisor: str, mensaje: str, es_grupal: bool) -> None:
        """
        Método para recibir mensaje de usuario
        id_emisor: id de quien envía el mensaje de chat
        nombre_emisor: quien envía el mensaje de chat
        mensaje: mensaje de usuario
        es_grupal: valida si es mensaje grupal
        """
        nombre_receptor = self.nombre
        if es_grupal:
            print(f"Mensaje Grupal: [Emisor]: {nombre_emisor} / [Receptor]: {nombre_receptor} - [Mensaje]: {mensaje}")
        else:
            print(f"Mensaje Directo: [Emisor]: {nombre_emisor} / [Receptor]: {nombre_receptor} - [Mensaje]: {mensaje}")
