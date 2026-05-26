"""
---------------------------------------------------------
Módulo: excepciones_personalizadas.py
---------------------------------------------------------
Este archivo contiene todas las excepciones personalizadas
utilizadas en el proyecto "Cazador de Contraseñas".

Las excepciones permiten manejar errores específicos
del juego de manera organizada y orientada a objetos.
---------------------------------------------------------
"""

class ErrorJuego(Exception):
    """
    Clase base para las excepciones del juego.
    Todas las excepciones personalizadas heredan de aquí.
    """

    pass

class LongitudInvalidaError(ErrorJuego):
    """
    Se lanza cuando la longitud ingresada
    es menor al mínimo permitido.
    """

    def __init__(self, mensaje="La longitud debe ser mínimo de 8 caracteres."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class EntradaNoNumericaError(ErrorJuego):
    """
    Se lanza cuando el usuario ingresa
    un valor que no es numérico.
    """

    def __init__(self, mensaje="Debe ingresar un número válido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ContraseñaInvalidaError(ErrorJuego):
    """
    Se lanza cuando la contraseña generada
    no cumple los requisitos establecidos.
    """

    def __init__(self, mensaje="La contraseña generada no es válida."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)