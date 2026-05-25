# ÍNDICE

* [1. EJERCICIO](#1-ejercicio)
    * [Escenario](#escenario)
    * [Problema](#problema)
    * [Beneficios](#beneficios-esperados-de-la-solución)
* [2. SOLUCIÓN](#2-solución)
    * [Análisis](#análisis)
    * [Decisiones](#decisiones)
      * [ADR](#adr-adopción-del-patrón-de-diseño-builder-para-la-creación-de-objetos-complejos)
      * [Contexto y Problema](#contexto-y-problema)
      * [Opciones Consideradas](#opciones-consideradas)
      * [Decisión Arquitectónica](#decisión-arquitectónica)
      * [Diagrama de Clases](#diagrama-de-clases)
      * [Consecuencias](#consecuencias)
* [3. MEJORA CONTINUA](#3-mejora-continua)

# 1. EJERCICIO

## Escenario:

Aplicación de chat grupal. Los usuarios pueden enviarse mensajes
entre sí dentro de una sala de chat. Sin embargo, gestionar las 
interacciones directas entre cada usuario haría que cada uno deba 
conocer y comunicarse con todos los demás, lo que resulta en una 
alta dependencia entre objetos.

## Problema:

Sin un mediador, cada usuario tendría que mantener referencias directas 
a todos los demás, lo que genera un sistema difícil de escalar y mantener. 
Si agregas o eliminas usuarios, debes actualizar muchas relaciones.

## Beneficios esperados de la Solución

- *Facilita el mantenimiento:* Agregar o eliminar usuarios no debe requerir 
modificar los demás.
- *Mejor organización:* La lógica de comunicación debe estar centralizada, 
no dispersa en muchos objetos.
- *Reduce la complejidad:* Evitar una red enmarañada de interacciones punto 
a punto.

---

# 2. SOLUCIÓN

## Análisis

Identifico un problema de comportamiento, razón por la cual acudo a los patrones 
comportamentales, y dado el problema podría suscribir los usuarios a un "canal"
para comunicarse entre sí que tal vez un patrón como Observer podría resolver, 
pero al escalar tendríamos una sobrecarga con las suscripciones mientras no se
están transmitiendo comunicaciones.

Analizando más a fondo el caso, la necesidad de un mediador encaja perfectamente 
con el patrón *mediator* con el que podemos orquestar el mensaje en lugar de
recibir peticiones continuas con un suscriptor sin tener un mensaje para entregar.

### Mediador

**Propósito:**

Te permite reducir las dependencias caóticas entre objetos. El patrón restringe 
las comunicaciones directas entre los objetos, forzándolos a colaborar 
únicamente a través de un objeto mediador.

**Se utiliza cuando:**
- Resulte difícil cambiar algunas de las clases porque están fuertemente 
acopladas a un puñado de otras clases.
- No puedas reutilizar un componente en un programa diferente porque sea 
demasiado dependiente de otros componentes
- Te encuentres creando cientos de subclases de componente sólo para 
reutilizar un comportamiento básico en varios contextos

---

## Decisiones

### ADR: Adopción del Patrón de Diseño Bridge para desacoplar abstracción e implementación

**Estado:** Aprobado  
**Fecha:** 22 de Mayo de 2026

#### Contexto y Problema

Necesitamos una solución que nos permita escalar en las interacciones entre objetos
para reutilizar comportamiento básico entre varios contextos de chat, ya que los
usuarios no sólo comparten en un chat grupal sino que también podrán comunicarse
entre ellos de manera directa.


#### Opciones Consideradas

1. Manejo de eventos simples: Considerar el uso de eventos nativo del lenguaje
de programación. Los mensajes serían gestionados a través del gestor de eventos
2. Funciones puras de entrega: Generar una clase de herramientas que solo reciba 
3 datos (ID_Origen, ID_Destino y Mensaje), orquestar con éstos IDs.

#### Decisión Arquitectónica

Se decide adoptar el **Patrón Mediator** para reducir las dependencias caóticas 
entre objetos (usuarios), colaborando exclusivamente a través de un objeto mediador
para la comunicación del mensaje, permitiendo encapsular la compleja red de 
relaciones entre varios objetos (usuario) dentro de un único objeto mediador. 
Cuantas menos dependencias tengo en la clase, más fácil es modificar, extender 
o reutilizar esa clase.

### Diagrama de Clases

A continuación el diagrama de clases en formato mermaid:

<div style="max-width: 85%; margin: 0 auto;">

```mermaid
classDiagram
    class ChatMediador {
        <<interface>>
        +registrar_usuario(usuario: UsuarioAbstracto)
        +enviar_mensaje_privado(id_emisor: str, id_receptor: str, mensaje: str)
        +enviar_mensaje_grupal(id_emisor: str, id_grupo: str, mensaje: str)
    }

    class ChatTextoMediador {
        -usuarios: dict [str, UsuarioAbstracto]
        -grupos: dict [str, list [str]]
        +registrar_usuario(usuario: Usuario)
        +crear_grupo(id_grupo: str, ids_usuarios: list [str])
        +enviar_mensaje_privado(id_emisor: str, id_receptor: str, mensaje: str)
        +enviar_mensaje_grupal(id_emisor: str, id_grupo: str, mensaje: str)
    }

    class UsuarioAbstracto {
        <<abstract>>
        -mediador: ChatMediador
        -id_usuario: str
        -nombre: str
        +enviar_mensaje_privado(id_receptor: str, mensaje: str)
        +enviar_mensaje_grupal(id_grupo: str, mensaje: str)
        +recibir_mensaje(id_emisor: str, nombre_emisor: str, mensaje: str, es_grupal: bool)*
    }

    class ChatUsuario {
        +enviar_mensaje_privado(id_receptor: str, mensaje: str)
        +enviar_mensaje_grupal(id_grupo: str, mensaje: str)
        +recibir_mensaje(id_emisor: str, nombre_emisor: str, mensaje: str, es_grupal: bool)
    }

    ChatMediador <|.. ChatTextoMediador : Implementa
    UsuarioAbstracto <|-- ChatUsuario : Hereda
    UsuarioAbstracto --> ChatMediador : Usa para enviar mensajes
    ChatTextoMediador --> UsuarioAbstracto : Guarda y notifica a
    
```
</div>

#### Consecuencias

**Ventajas**
- *Menor acoplamiento:* Los usuarios no necesitan conocer la existencia de los 
otros usuarios en memoria. Solo conocen al Mediador.
- *Facilidad para escalar:* Si agregas un usuario nuevo, no tienes que actualizar 
a los demás usuarios. Solo registras al nuevo en el Mediador.
- *Reutilización de código:* Puedes cambiar las reglas de cómo se envían los 
mensajes en un solo lugar.

**Desventajas**

- *Punto único de falla:* Si el Mediador falla, todo el sistema de chat se cae 
por completo.
- *Complejidad centralizada:* Con el tiempo, el Mediador puede volverse muy grande 
y difícil de mantener si le agregas demasiadas tareas.
- *Cuello de botella:* Si miles de usuarios envían mensajes al mismo tiempo, el 
Mediador puede saturarse si no está bien optimizado.

## 3. MEJORA CONTINUA

Dado que el en la interfaz mediador requerirá de la clase abastracta Usuario la cual también 
utiliza la implementación concreta del mediador (ChatTextoMediador) se presentará una referencia 
circular entre ambos que detectará el IDE y el intérprete de Python, por ésta razón, debo hacer 
uso de una especie de filtro para que el interprete no lo evalué previamente a la construcción 
del objeto, para ello tengo 2 opciones de gestionarlo:

1. Usar ***from __future__import annotations***:

- Cuando estoy trabajando en un solo archivo y una clase necesita hacer referencia a sí misma
(por ejemplo, un método dentro de Usuario que reciba a otro Usuario)
- Cuando quiera usar nombres de clases que están definidas más abajo en el mismo archivo

2. Usar ***TYPE_CHECKING***:

- Cuando tengo un archivo *"archivo_A.py"* que necesita saber el tipo de una clase en 
*"archivo_B.py"* y el archivo *"archivo_B.py"* necesita saber el tipo de una clase en 
archivo *"archivo_A.py"*. **< referencia circular >** conectar 2 clases concretas que dependen
entre si.
- Cuando quiero un código súper limpio y *no quiero crear un archivo intermedio* como el de 
*"interfaces.py"*

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Esto SOLO lo lee tu editor de código (VS Code, PyCharm, etc.)
    # El motor de Python IGNORA por completo esta línea al correr el programa
    from usuario import ChatUsuario 
```

### Diferencias 

| Característica | `from __future__ import annotations` | `TYPE_CHECKING` |
| :--- | :--- | :--- |
| **¿Qué hace?** | Convierte las pistas de tipo en cadenas de texto en todo el archivo. | Permite importar archivos en un bloque oculto solo para el editor. |
| **¿Evita la carga del archivo?** | **No**. Si importas el archivo arriba, Python intentará cargarlo de todos modos. | **Sí**. Evita que Python cargue el archivo importado cuando ejecutas el código. |
| **Uso principal** | Evitar errores cuando una clase se referencia a sí misma o no se ha definido abajo. | Romper de raíz las importaciones circulares entre archivos diferentes. |

