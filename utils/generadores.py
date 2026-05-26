"""
---------------------------------------------------------
Módulo: generadores.py
---------------------------------------------------------
Este archivo contiene funciones auxiliares utilizadas
en el juego "Cazador de Contraseñas".

Funciones:
- Generación aleatoria de cofres
- Probabilidades de aparición
---------------------------------------------------------
"""

# ==================================================
# IMPORTACIONES
# ==================================================

import random

from clases.cofre import (
    CofreComun,
    CofreRaro,
    CofreLegendario
)

# ==================================================
# FUNCIÓN GENERADORA DE COFRES
# ==================================================

def generar_cofre_aleatorio():
    """
    Genera un cofre aleatorio basado en probabilidades.

    Probabilidades:
    - Común: 60%
    - Raro: 30%
    - Legendario: 10%

    Retorna:
        objeto Cofre
    """

    cofres = [
        CofreComun(),
        CofreRaro(),
        CofreLegendario()
    ]

    probabilidades = [60, 30, 10]

    return random.choices(
        cofres,
        weights=probabilidades,
        k=1
    )[0]