from Libro import Libro
from Revista import Revista
# Importamos las funciones de tu archivo de utilidades

from Utils import (
    crear_menu, 
    leer_cadena, 
    leer_int, 
    leer_nombre_archivo,
    guardar_publicaciones, 
    cargar_publicaciones, 
    mostrar_lista_publicaciones
)
from excepciones import ErrorArchivo

def main():
    # Esta lista almacenará los objetos (Libros y Revistas) en memoria
    biblioteca = []
    
    opciones = [
        "Añadir publicación",
        "Mostrar publicaciones disponibles",
        "Guardar publicaciones en un fichero",
        "Cargar publicaciones desde un fichero",
        "Salir"
    ]

    while True:
        # Usamos la función del menú que ya tienes en utilsB
        opcion = crear_menu(opciones)

        # OPCIÓN 1: AÑADIR
        if opcion == 1:
            print("\n--- NUEVA PUBLICACIÓN ---")
            try:
                # Sub-selección simple
                tipo = leer_int("¿Qué deseas añadir? (1: Libro, 2: Revista): ")
                
                if tipo not in [1, 2]:
                    print("❌ Tipo no válido. Volviendo al menú.")
                    continue

                # Pedimos datos comunes (Publicacion)
                titulo = leer_cadena("Título: ")
                autor = leer_cadena("Autor: ")
                anio = leer_int("Año de publicación: ")

                if tipo == 1: # Libro
                    genero = leer_cadena("Género: ")
                    # Instanciamos el objeto
                    nuevo_obj = Libro(titulo, autor, anio, genero)
                else: # Revista
                    num_edicion = leer_int("Número de edición: ")
                    # Instanciamos el objeto
                    nuevo_obj = Revista(titulo, autor, anio, num_edicion)
                
                # Si todo ha ido bien, lo guardamos en la lista
                biblioteca.append(nuevo_obj)
                print("✅ Publicación registrada correctamente.")

            except ValueError as e:
                # Capturamos errores de validación de las clases (setters)
                print(f"❌ Error en los datos: {e}")
            except Exception as e:
                print(f"❌ Error inesperado: {e}")

        # OPCIÓN 2: MOSTRAR
        elif opcion == 2:
            mostrar_lista_publicaciones(biblioteca)

        # OPCIÓN 3: GUARDAR
        elif opcion == 3:
            if not biblioteca:
                print("⚠️ No hay datos para guardar.")
            else:
                nombre = leer_nombre_archivo("Nombre del fichero para guardar (ej. datos.json): ")
                try:
                    guardar_publicaciones(biblioteca, nombre)
                except ErrorArchivo as e:
                    print(f"❌ {e}")

        # OPCIÓN 4: CARGAR
        # OPCIÓN 4: CARGAR
        elif opcion == 4:
            nombre = leer_nombre_archivo("Nombre del fichero a cargar: ")
            try:
                nuevos_datos = cargar_publicaciones(nombre)
                
                # --- CAMBIO AQUÍ ---
                if len(biblioteca) > 0:
                    print(f"⚠️ Tienes {len(biblioteca)} publicaciones en memoria.")
                    # Reutilizamos tu función leer_int para el menú
                    decision = leer_int("¿Quieres sobrescribir (1) o fusionar/añadir (2)? ")
                    
                    if decision == 1:
                        biblioteca = nuevos_datos # Sobrescribe (comportamiento original)
                        print("🗑️ Memoria anterior borrada. Datos nuevos cargados.")
                    else:
                        biblioteca.extend(nuevos_datos) # Fusiona
                        print("➕ Datos añadidos a la lista existente.")
                else:
                    # Si la lista estaba vacía, cargamos directamente
                    biblioteca = nuevos_datos
                # -------------------

            except ErrorArchivo as e:
                print(f"❌ {e}")

        # OPCIÓN 5: SALIR
        elif opcion == 5:
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()