"""utilsB.py contiene las funciones extras necesarias para el main"""

import json
import os
from typing import List, Any
from excepciones import ErrorArchivo

# ==================== VALIDACIONES (INPUT) ====================

def leer_cadena(mensaje: str) -> str:
    """Lee una cadena no vacía."""
    while True:
        cadena = input(mensaje).strip()
        if cadena:
            return cadena
        print("❌ Error: Este campo no puede estar vacío.")

def leer_int(mensaje: str) -> int:
    """Lee un entero positivo."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("❌ Error: El número debe ser positivo.")
        except ValueError:
            print("❌ Error: Debes introducir un número entero válido.")

def leer_nombre_archivo(mensaje: str) -> str:
    """Lee un nombre de archivo y asegura la extensión .json."""
    nombre = leer_cadena(mensaje)
    if not nombre.endswith('.json'):
        nombre += '.json'
    return nombre

# ==================== MENÚ ====================

def crear_menu(opciones: List[str]) -> int:
    """Muestra menú y devuelve opción válida."""
    print("\n" + "="*30)
    print("      MENÚ BIBLIOTECA")
    print("="*30)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    print("="*30)
    
    while True:
        try:
            opcion = int(input(f"Selecciona una opción (1-{len(opciones)}): "))
            if 1 <= opcion <= len(opciones):
                return opcion
            print("Opción fuera de rango.")
        except ValueError:
            print("Introduce un número válido.")

# ==================== PERSISTENCIA (JSON) ====================

def guardar_publicaciones(publicaciones: List[Any], nombre_archivo: str):
    """Guarda la lista completa de objetos en JSON."""
    try:
        datos = []
        for pub in publicaciones:
            # Detectamos el tipo basándonos en si tiene atributo 'genero'
            es_libro = hasattr(pub, 'genero') 
            
            diccionario = {
                "tipo": "Libro" if es_libro else "Revista",
                "titulo": pub.titulo,
                "autor": pub.autor,
                "anio": pub.anio
            }
            
            if es_libro:
                diccionario["genero"] = pub.genero
            else:
                diccionario["num_edicion"] = pub.num_edicion
            
            datos.append(diccionario)

        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
            
        print(f"✅ Se han guardado {len(datos)} publicaciones en '{nombre_archivo}'.")

    except Exception as e:
        # Envolvemos cualquier error en nuestra excepción personalizada
        raise ErrorArchivo(f"Error al guardar el archivo: {e}")

def cargar_publicaciones(nombre_archivo: str) -> List[Any]:
    """Lee JSON y devuelve lista de objetos Libro/Revista."""
    # Importación local para evitar dependencia circular
    from Libro import Libro
    from Revista import Revista

    if not os.path.exists(nombre_archivo):
        raise ErrorArchivo(f"El archivo '{nombre_archivo}' no existe.")

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)

        lista_objs = []
        for item in datos:
            if item["tipo"] == "Libro":
                obj = Libro(item["titulo"], item["autor"], item["anio"], item["genero"])
            elif item["tipo"] == "Revista":
                obj = Revista(item["titulo"], item["autor"], item["anio"], item["num_edicion"])
            else:
                continue # Saltamos tipos desconocidos
            
            lista_objs.append(obj)
            
        print(f"✅ Se han cargado {len(lista_objs)} publicaciones.")
        return lista_objs

    except json.JSONDecodeError:
        raise ErrorArchivo("El archivo está corrupto o no es un JSON válido.")
    except KeyError as e:
        raise ErrorArchivo(f"Faltan datos obligatorios en el archivo: {e}")
    except Exception as e:
        raise ErrorArchivo(f"Error inesperado leyendo: {e}")

# ==================== UI / VISUALIZACIÓN ====================

def mostrar_lista_publicaciones(publicaciones: List[Any]):
    if not publicaciones:
        print("\n📭 No hay publicaciones registradas.")
        return

    print("\n--- LISTADO DE PUBLICACIONES ---")
    for pub in publicaciones:
        print(pub.descripcion()) # Polimorfismo: llama al descripcion() de cada objeto
        print("-" * 20)