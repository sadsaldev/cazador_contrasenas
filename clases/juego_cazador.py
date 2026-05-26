"""
---------------------------------------------------------
Módulo: juego_cazador.py
---------------------------------------------------------
Este archivo contiene la clase JuegoCazador,
encargada de controlar toda la lógica principal
del juego "Cazador de Contraseñas".

Funciones principales:
- Controlar rondas
- Administrar puntaje
- Manejar excepciones
- Generar cofres aleatorios
- Permitir múltiples partidas
---------------------------------------------------------
"""

# ==================================================
# IMPORTACIONES
# ==================================================

import random

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from clases.contraseña import Contraseña

from clases.cofre import (
    CofreComun,
    CofreRaro,
    CofreLegendario,
    CofreMaldito
)

from excepciones.excepciones_personalizadas import (
    LongitudInvalidaError,
    EntradaNoNumericaError,
    ContraseñaInvalidaError
)

from utils.generadores import generar_cofre_aleatorio

# ==================================================
# CLASE PRINCIPAL DEL JUEGO
# ==================================================

class JuegoCazador:
    """
    Clase principal encargada de controlar
    el flujo del juego.
    """

    def __init__(self):
        """
        Constructor de la clase JuegoCazador.
        """

        self.__puntaje = 0
        self.__jugando = True
        self.__console = Console()
        self.__ronda = 1

    # ==================================================
    # MÉTODOS PRIVADOS
    # ==================================================

    def __solicitar_longitud(self):
        """
        Solicita al usuario la longitud deseada.

        Retorna:
            int
        """

        entrada = input(
            "\nIngrese la longitud de la contraseña: "
        )

        if not entrada.isdigit():
            raise EntradaNoNumericaError()

        return int(entrada)

    def __mostrar_resultado(
        self,
        password,
        nombre_cofre,
        puntos,
        mensaje
    ):
        """
        Muestra visualmente el resultado de la ronda.
        """

        color_cofre = "white"

        if "Común" in nombre_cofre:
            color_cofre = "green"

        elif "Raro" in nombre_cofre:
            color_cofre = "magenta"

        elif "Legendario" in nombre_cofre:
            color_cofre = "yellow"

        elif "Maldito" in nombre_cofre:
            color_cofre = "red"

        tabla = Table(title="\nResultado de la Ronda")

        tabla.add_column("Elemento", style="cyan")
        tabla.add_column("Valor", style="magenta")
        tabla.add_row("Contraseña", password)
        tabla.add_row("Cofre", f"[bold {color_cofre}]{nombre_cofre}[/bold {color_cofre}]")
        tabla.add_row("Puntos", str(puntos))
        tabla.add_row("Mensaje", mensaje)
        tabla.add_row("Puntaje Total", str(self.__puntaje))
        tabla.add_row("Ronda", str(self.__ronda))

        self.__console.print(tabla)


    def __preguntar_continuar(self):
        """
        Pregunta al usuario si desea continuar.
        """

        while True:

            opcion = input(
                "\n¿Desea jugar otra ronda? (s/n): "
            ).lower()

            if opcion in ["s", "n"]:

                if opcion == "n":
                    self.__jugando = False

                break

            self.__console.print(
                "[bold red]Opción inválida. "
                "Ingrese 's' o 'n'.[/bold red]"
            )

    # ==================================================
    # MÉTODO PRINCIPAL
    # ==================================================

    def iniciar_juego(self):
        """
        Inicia el juego principal.
        """

        titulo = Panel.fit(
            "[bold cyan]CAZADOR DE CONTRASEÑAS[/bold cyan]\n"
            "[white]Juego POO en Python[/white]",
            border_style="bright_blue"
        )

        self.__console.print(titulo)

        self.__console.print(
            "[bold white]Reglas del juego:[/bold white]"
        )

        self.__console.print(
            "- Longitud mínima: 8 caracteres"
        )

        self.__console.print(
            "- Debe contener mayúsculas, minúsculas, números y símbolos"
        )

        self.__console.print(
            "- No se permiten caracteres repetidos\n"
        )

        while self.__jugando:
            self.__console.rule(
                f"[bold cyan]RONDA {self.__ronda}"
            )

            try:

                # Solicitar longitud
                longitud = self.__solicitar_longitud()

                # Crear contraseña
                password = Contraseña(longitud)

                # Generar password
                password.generar_password()

                # Validar password
                if password.validar_password():

                    # Generar cofre positivo
                    cofre = generar_cofre_aleatorio()

                else:
                    raise ContraseñaInvalidaError()

            except (
                LongitudInvalidaError,
                EntradaNoNumericaError,
                ContraseñaInvalidaError

            ) as error:

                self.__console.print(
                    f"\n[bold red]ERROR:[/bold red] {error}"
                )

                # Cofre maldito
                cofre = CofreMaldito()

                password_texto = "INVÁLIDA"

            else:

                password_texto = password.obtener_password()

            finally:

                # Abrir cofre
                nombre, puntos, mensaje = cofre.abrir()

                # Actualizar puntaje
                self.__puntaje += puntos

                # Mostrar resultado
                self.__mostrar_resultado(
                    password_texto,
                    nombre,
                    puntos,
                    mensaje
                )

                self.__ronda += 1

                # Continuar o salir
                self.__preguntar_continuar()

        print()
        panel_final = Panel.fit(
            f"[bold green]Gracias por jugar[/bold green]\n\n"
            f"[yellow]Puntaje final:[/yellow] {self.__puntaje}",
            border_style="green"
        )

        self.__console.print(panel_final)
   