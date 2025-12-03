# excepciones.py
class ErrorBiblioteca(Exception):
    """Excepción base para errores en la biblioteca"""
    def __init__(self, mensaje="Error en la biblioteca"):
        super().__init__(mensaje)
        self.mensaje = mensaje
    
    def __str__(self):
        return self.mensaje


class ErrorArchivo(ErrorBiblioteca):
    """Excepción para problemas relacionados con ficheros"""
    def __init__(self, mensaje="Error al manejar el archivo"):
        super().__init__(mensaje)