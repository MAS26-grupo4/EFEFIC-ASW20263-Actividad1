from src.chats.chat_texto_mediador import ChatTextoMediador
from src.usuarios.chat_usuario import ChatUsuario

def main():
    # 1. Instanciar el mediador central
    sala_chat = ChatTextoMediador()

    # 2. Instanciar componentes (usuarios) pasándoles el mediador
    juan = ChatUsuario(sala_chat, "usr_1", "Juan")
    maria = ChatUsuario(sala_chat, "usr_2", "María")
    pedro = ChatUsuario(sala_chat, "usr_3", "Pedro")
    ana = ChatUsuario(sala_chat, "usr_4", "Ana")

    # 3. Registrar los componentes en el mediador
    sala_chat.registrar_usuario(juan)
    sala_chat.registrar_usuario(maria)
    sala_chat.registrar_usuario(pedro)
    sala_chat.registrar_usuario(ana)

    # 4. Crear grupos de chat
    sala_chat.crear_grupo("grupo_1", ["usr_1", "usr_3", "usr_4"])

    # 5. Ejecutar acciones
    print("--- 💬 Prueba de Chat Separado ---\n")
    juan.enviar_mensaje_privado("usr_2", "Hola María, éste es nuestro mensaje privado.")
    maria.enviar_mensaje_privado("usr_1", "Hola Juan, confirmo mensaje privado.")
    print("-" * 50)
    pedro.enviar_mensaje_grupal("grupo_1", "¡Hola grupo!, éste es nuestro mensaje grupal.")
    juan.enviar_mensaje_grupal("grupo_1", "confirmo llegada de mensaje grupal.")

if __name__ == "__main__":
    main()
