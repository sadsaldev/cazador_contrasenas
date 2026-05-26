"""
---------------------------------------------------------
Proyecto: Cazador de Contraseñas
---------------------------------------------------------
Autor: Salomé Londoño M.
# Asignatura: Programación
Programa: Ingeniería de Sistemas
Institución: Universidad Nacional Abierta y a Distancia


Descripción:
Juego interactivo desarrollado en Python utilizando
Programación Orientada a Objetos.

El jugador genera contraseñas aleatorias válidas
para abrir cofres y acumular puntos.

El proyecto implementa:
- Clases y objetos
- Herencia
- Polimorfismo
- Encapsulamiento
- Manejo de excepciones
- Aleatoriedad
---------------------------------------------------------
"""

# ==================================================
# IMPORTACIONES
# ==================================================

from clases.juego_cazador import JuegoCazador

# ==================================================
# FUNCIÓN PRINCIPAL
# ==================================================

def main():
    """
    Función principal del programa.
    """

    juego = JuegoCazador()
    juego.iniciar_juego()

# ==================================================
# EJECUCIÓN DEL PROGRAMA
# ==================================================

if __name__ == "__main__":
    main()