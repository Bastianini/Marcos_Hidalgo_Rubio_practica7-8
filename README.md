# Práctica 7-8: Gestión de Biblioteca Digital

Este repositorio contiene la implementación de un sistema de gestión de bibliotecas en Python. El proyecto utiliza conceptos de Programación Orientada a Objetos (POO) como herencia, polimorfismo, encapsulamiento y persistencia de datos mediante ficheros JSON.

## Estructura del Proyecto

* **Publicacion.py**: Clase base con atributos comunes (título, autor, año).
* **Libro.py**: Clase derivada que añade género.
* **Revista.py**: Clase derivada que añade número de edición.
* **Utils.py**: Funciones auxiliares para menús, validaciones y manejo de ficheros JSON.
* **excepciones.py**: Definición de excepciones personalizadas (`ErrorBiblioteca`, `ErrorArchivo`).
* **main.py**: Punto de entrada del programa con el menú principal.

---

## Registro de Consultas a LLMs

Para el desarrollo de esta práctica se utilizó un Asistente de IA (LLM) para resolver dudas conceptuales y de implementación. A continuación se detallan 7 preguntas clave realizadas durante el proceso:

### 1. ¿Cómo puedo diferenciar un `Libro` de una `Revista` al guardarlos en un mismo JSON?
**Respuesta del LLM:**
Dado que JSON no almacena el tipo de clase de Python, es necesario añadir un campo discriminador al diccionario antes de guardarlo. Al serializar el objeto en `guardar_publicaciones`, se añadió un campo `"tipo": "Libro"` o `"tipo": "Revista"`. Al leer el archivo de vuelta, se comprueba este campo para decidir si instanciar la clase `Libro` o la clase `Revista` con los datos correspondientes.

### 2. ¿Por qué se usan decoradores `@property` en la clase `Publicacion`?
**Respuesta del LLM:**
Se utilizan para implementar el encapsulamiento de forma "Pythonica". Permiten acceder a los atributos como si fueran variables públicas (ej. `obj.titulo`), pero ejecutando métodos *getter* y *setter* por debajo. Esto es fundamental en esta práctica para incluir validaciones en el *setter* (como asegurar que el título no esté vacío) sin cambiar la sintaxis de acceso en el resto del código.

### 3. Tengo un error de "ImportError circular" entre `Utils.py` y las clases `Libro`/`Revista`. ¿Cómo se soluciona?
**Respuesta del LLM:**
Esto ocurre porque `main` importa `Utils`, y si `Utils` intenta importar `Libro` al principio del archivo, se crea un ciclo si `Libro` también depende indirectamente de algo que ya se está cargando. La solución recomendada fue realizar la importación dentro de la función `cargar_publicaciones` (importación local) en lugar de al inicio del archivo, rompiendo así el ciclo de dependencias al cargar el módulo.

### 4. ¿Cómo funciona el polimorfismo en el método `mostrar_lista_publicaciones`?
**Respuesta del LLM:**
El polimorfismo permite tratar objetos de diferentes clases (Libro y Revista) de manera uniforme porque ambas heredan de `Publicacion`. En el bucle que recorre la lista, se llama al método `.descripcion()` de cada objeto. Python determina en tiempo de ejecución cuál versión del método ejecutar (la de `Libro` que muestra el género o la de `Revista` que muestra la edición), sin necesidad de usar `if/else` para comprobar el tipo de cada objeto.

### 5. Al cargar datos desde el fichero, se borran los libros que acababa de añadir en memoria. ¿Cómo lo arreglo?
**Respuesta del LLM:**
El problema estaba en la asignación `biblioteca = nuevos_datos`, que reemplazaba completamente la lista existente. La solución fue utilizar el método `.extend(nuevos_datos)` sobre la lista `biblioteca`. De esta forma, los objetos leídos del fichero se añaden al final de la lista actual, permitiendo fusionar los datos en memoria con los del archivo.

### 6. ¿Qué ventaja tiene crear una excepción personalizada `ErrorArchivo` en lugar de usar `IOError`?
**Respuesta del LLM:**
Crear `ErrorArchivo` (que hereda de `ErrorBiblioteca` y esta de `Exception`) permite tener un control más granular de los errores específicos de nuestra lógica de negocio. Nos permite capturar errores de lectura/escritura y envolverlos en un mensaje más amigable para el usuario final en el `main`, separando los errores técnicos de Python de los errores semánticos de nuestra aplicación.

### 7. ¿Cómo puedo validar que el año introducido sea un entero positivo sin que el programa se cierre si el usuario escribe texto?
**Respuesta del LLM:**
Se implementó una función auxiliar `leer_int` en `Utils.py` que utiliza un bucle `while True` y un bloque `try-except ValueError`. Si el usuario introduce texto, el `except` captura el error y pide el dato de nuevo. Si introduce un número, un `if valor > 0` verifica que sea positivo. El programa no avanza hasta recibir un dato válido, garantizando la robustez de la aplicación.
