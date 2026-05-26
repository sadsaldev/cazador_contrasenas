"""
---------------------------------------------------------
Módulo: contraseña.py
---------------------------------------------------------
Este archivo contiene la clase Contraseña, encargada
de generar y validar contraseñas aleatorias para el
juego "Cazador de Contraseñas".

La contraseña debe cumplir las siguientes reglas:
- Longitud mínima de 8 caracteres
- Al menos una mayúscula
- Al menos una minúscula
- Al menos un número
- Al menos un carácter especial
- No debe contener caracteres repetidos
---------------------------------------------------------
"""

# =========================
# IMPORTACIONES
# =========================

import random
import string

from excepciones.excepciones_personalizadas import (
    LongitudInvalidaError,
    ContraseñaInvalidaError
)

# =========================
# CLASE CONTRASEÑA
# =========================

class Contraseña:
    """
    Clase encargada de generar y validar contraseñas.
    """

    # Caracteres especiales permitidos
    CARACTERES_ESPECIALES = "¿¡?=)(/¨*+-%&$#!"

    def __init__(self, longitud):
        """
        Constructor de la clase.

        Parámetros:
            longitud (int): longitud deseada para la contraseña.
        """

        self.__longitud = longitud
        self.__password = ""

        # Validar longitud al crear el objeto
        self.__validar_longitud()

    # ==================================================
    # MÉTODOS PRIVADOS
    # ==================================================

    def __validar_longitud(self):
        """
        Verifica que la longitud sea válida.
        """

        if self.__longitud < 8:
            raise LongitudInvalidaError()

    def __tiene_repetidos(self, texto):
        """
        Verifica si existen caracteres repetidos.

        Parámetros:
            texto (str): cadena a evaluar.

        Retorna:
            bool
        """

        return len(texto) != len(set(texto))

    # ==================================================
    # MÉTODOS PÚBLICOS
    # ==================================================

    def generar_password(self):
        """
        Genera una contraseña aleatoria válida.
        """

        mayuscula = random.choice(string.ascii_uppercase)
        minuscula = random.choice(string.ascii_lowercase)
        numero = random.choice(string.digits)
        especial = random.choice(self.CARACTERES_ESPECIALES)

        # Conjunto general de caracteres válidos
        todos_caracteres = (
            string.ascii_letters +
            string.digits +
            self.CARACTERES_ESPECIALES
        )

        # Convertir en set para evitar repetidos
        usados = {mayuscula, minuscula, numero, especial}

        password_lista = [mayuscula, minuscula, numero, especial]

        # Completar caracteres restantes
        while len(password_lista) < self.__longitud:

            caracter = random.choice(todos_caracteres)

            if caracter not in usados:
                password_lista.append(caracter)
                usados.add(caracter)

        # Mezclar posiciones aleatoriamente
        random.shuffle(password_lista)

        # Convertir lista en string
        self.__password = "".join(password_lista)

        # Validar la contraseña generada
        if not self.validar_password():
            raise ContraseñaInvalidaError()

    def validar_password(self):
        """
        Verifica que la contraseña cumpla todos
        los requisitos establecidos.

        Retorna:
            bool
        """

        password = self.__password

        tiene_mayuscula = any(c.isupper() for c in password)
        tiene_minuscula = any(c.islower() for c in password)
        tiene_numero = any(c.isdigit() for c in password)

        tiene_especial = any(
            c in self.CARACTERES_ESPECIALES
            for c in password
        )

        sin_repetidos = not self.__tiene_repetidos(password)

        return (
            len(password) >= 8 and
            tiene_mayuscula and
            tiene_minuscula and
            tiene_numero and
            tiene_especial and
            sin_repetidos
        )

    def obtener_password(self):
        """
        Devuelve la contraseña generada.

        Retorna:
            str
        """

        return self.__password