from Publicacion import Publicacion

class Revista(Publicacion):
    def __init__(self, titulo: str, autor: str, anio: int, num_edicion: int):
        """
        Inicializa una revista con título, autor, año y número de edición
        
        Args:
            titulo (str): Título de la revista
            autor (str): Autor/Editor de la revista
            anio (int): Año de publicación
            num_edicion (int): Número de edición
        """
        super().__init__(titulo, autor, anio)
        self._num_edicion = num_edicion
    
    # Decorador para el atributo adicional
    @property
    def num_edicion(self):
        """Obtiene el número de edición de la revista"""
        return self._num_edicion
    
    @num_edicion.setter
    def num_edicion(self, valor: int):
        """Establece el número de edición de la revista"""
        if not isinstance(valor, int):
            raise ValueError("El número de edición debe ser un entero")
        if valor <= 0:
            raise ValueError("El número de edición debe ser positivo")
        self._num_edicion = valor
    
    def descripcion(self):
        """
        Muestra los datos de la revista (redefinición del método base)
        """
        return f"Revista: {super().descripcion()}, Edición: {self._num_edicion}"