"""
---------------------------------------------------------
Módulo: cofre.py
---------------------------------------------------------
Este archivo contiene las clases relacionadas con los
cofres del juego "Cazador de Contraseñas".

Cada cofre otorga o resta puntos dependiendo de su tipo:
- Común
- Raro
- Legendario
- Maldito

Se implementa herencia y polimorfismo mediante una clase
base llamada Cofre.
---------------------------------------------------------
"""

# ==================================================
# CLASE PADRE
# ==================================================

class Cofre:
    """
    Clase base para todos los cofres del juego.
    """

    def __init__(self, nombre, puntos, mensaje):
        """
        Constructor de la clase Cofre.

        Parámetros:
            nombre (str): nombre del cofre.
            puntos (int): puntos que otorga o resta.
            mensaje (str): mensaje descriptivo.
        """

        self._nombre = nombre
        self._puntos = puntos
        self._mensaje = mensaje

    def abrir(self):
        """
        Devuelve la información del cofre.

        Retorna:
            tuple
        """

        return (
            self._nombre,
            self._puntos,
            self._mensaje
        )


# ==================================================
# COFRE COMÚN
# ==================================================

class CofreComun(Cofre):
    """
    Cofre de baja rareza.
    """

    def __init__(self):

        super().__init__(
            "Cofre Común",
            10,
            "Has encontrado un cofre común."
        )


# ==================================================
# COFRE RARO
# ==================================================

class CofreRaro(Cofre):
    """
    Cofre de rareza media.
    """

    def __init__(self):

        super().__init__(
            "Cofre Raro",
            25,
            "¡Excelente! Has abierto un cofre raro."
        )


# ==================================================
# COFRE LEGENDARIO
# ==================================================

class CofreLegendario(Cofre):
    """
    Cofre de máxima rareza.
    """

    def __init__(self):

        super().__init__(
            "Cofre Legendario",
            50,
            "¡INCREÍBLE! Has desbloqueado un cofre legendario."
        )


# ==================================================
# COFRE MALDITO
# ==================================================

class CofreMaldito(Cofre):
    """
    Cofre de penalización.
    """

    def __init__(self):

        super().__init__(
            "Cofre Maldito",
            -20,
            "La contraseña fue inválida. Has caído en un cofre maldito."
        )