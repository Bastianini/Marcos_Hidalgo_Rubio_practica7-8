from Publicacion import Publicacion

class Libro(Publicacion):
    def __init__(self, titulo: str, autor: str, anio: int, genero: str):
        """
        Inicializa un libro con título, autor, año y género
        
        Args:s
            titulo (str): Título del libro
            autor (str): Autor del libro
            anio (int): Año de publicación
            genero (str): Género del libro
        """
        super().__init__(titulo, autor, anio)
        self._genero = genero
    
    # Decorador para el atributo adicional
    @property
    def genero(self):
        """Obtiene el género del libro"""
        return self._genero
    
    @genero.setter
    def genero(self, valor: str):
        """Establece el género del libro"""
        if not valor or not valor.strip():
            raise ValueError("El género no puede estar vacío")
        self._genero = valor
    
    def descripcion(self):
        """
        Muestra los datos del libro (redefinición del método base)
        """
        return f"Libro: {super().descripcion()}, Género: {self._genero}"