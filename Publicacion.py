class Publicacion:
    """Clase publicación"""
    def __init__(self, titulo = "", autor = "", anio = 0):
        #atributos protegidos
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

    #Decoradores
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, valor):
        if not valor or not valor.strip():
            raise ValueError ("El titulo no puede estar vacio")
        self._titulo = valor.strip()
    
    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El autor no puede estar vacío")
        self._autor = valor.strip()
    
    @property
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self, valor):
        if not isinstance(valor, int):
            raise ValueError ("El año debe ser un numero entero")
        if valor <= 0:
            raise ValueError("El año debe ser un numero positivo")
        self._anio = valor

    def descripcion(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Año de publicacion: {self._anio}"

