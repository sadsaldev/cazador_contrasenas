# JUEGO CAZADOR DE CONTRASEÑAS

## Descripción del proyecto

"Cazador de Contraseñas" es un juego interactivo desarrollado en Python utilizando Programación Orientada a Objetos (POO).

El objetivo del juego es generar contraseñas aleatorias válidas para abrir cofres y acumular puntos. Dependiendo de la calidad de la contraseña generada, el jugador puede obtener distintos tipos de cofres con recompensas positivas o negativas.

El proyecto implementa:
- Programación Orientada a Objetos
- Herencia
- Polimorfismo
- Encapsulamiento
- Manejo de excepciones personalizadas
- Aleatoriedad
- Modularidad
- Interfaz visual en consola con Rich


---

# Objetivos del proyecto

- Aplicar conceptos de Programación Orientada a Objetos.
- Implementar generación aleatoria de contraseñas.
- Validar reglas estrictas de seguridad.
- Manejar errores mediante excepciones personalizadas.
- Desarrollar un sistema modular y escalable.
- Mejorar la experiencia visual en consola.


---

# Requisitos de la contraseña

Cada contraseña generada debe cumplir obligatoriamente:

- Longitud mínima de 8 caracteres.
- Contener al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un número,
  - un carácter especial.
- No contener caracteres repetidos.
- Tener posiciones aleatorias sin patrones predecibles.


---

# Tecnologías utilizadas

- Python 3
- Librería Rich


---

# Instalación

1. Clonar o descargar el proyecto

```bash

git clone https://github.com/sadsaldev/cazador_contrasenas

```

O descargar manualmente los archivos.

2. Instalar dependencias

```bash

pip install rich

```

---


# Ejecución del programa

Desde la carpeta principal del proyecto ejecutar:

python main.py


---

# Estructura del proyecto

cazador_contrasenas/
│
├── main.py
│
├── clases/
│   ├── contraseña.py
│   ├── cofre.py
│   ├── juego_cazador.py
│
├── excepciones/
│   ├── excepciones_personalizadas.py
│
├── utils/
│   ├── generadores.py
│
└── README.md


---

# Estructura del proyecto

## Clase Contraseña

Archivo:

clases/contraseña.py

**Responsabilidades:**

- Generar contraseñas aleatorias.
- Validar requisitos de seguridad.
- Evitar caracteres repetidos.
- Gestionar la longitud mínima.


**Métodos principales**

- generar_password() -> Genera la contraseña
- validar_password() -> Verifica requisitos
- obtener_password() -> Devuelve la contraseña


## Clase Cofre

Archivo:

clases/cofre.py

Representa los distintos cofres del juego.

**Tipos de cofres**

- Cofre Común -> +10 pts.
- Cofre Raro -> +25 pts.
- Cofre Legendario -> +50 pts.
- Cofre Maldito -> -20 pts.


**Herencia implementada**

Cofre
 ├── CofreComun
 ├── CofreRaro
 ├── CofreLegendario
 └── CofreMaldito


## Clase Juego Cazador

Archivo:

clases/juego_cazador.py

Controla toda la lógica principal del juego:

- rondas,
- puntajes,
- generación de cofres,
- manejo de errores,
- interacción con el usuario.


---

# Manejo de excepciones

El proyecto implementa excepciones personalizadas para mejorar la robustez del sistema.

**Excepciones utilizadas**

- **LongitudInvalidaError:** Longitud menor a 8
- **EntradaNoNumericaError:** Entrada inválida
- **ContraseñaInvalidaError:** Contraseña incorrecta

Archivo:

excepciones/excepciones_personalizadas.py


---

# Conceptos de Programación Orientada a Objetos aplicados

## Encapsulamiento

Uso de atributos privados:

self.__puntaje
self.__password


## Herencia

Los distintos cofres heredan de una clase base llamada Cofre.


## Polimorfismo

Todos los cofres utilizan el método:

abrir()

pero cada uno presenta un comportamiento diferente.


## Abstracción

Cada clase tiene responsabilidades específicas:

- Contraseña → generación y validación.
- Cofre → recompensas y penalizaciones.
- JuegoCazador → flujo principal.


---

# Funcionalidades principales

- Funcionalidades principales
- Generación aleatoria de contraseñas.
- Validación automática.
- Cofres aleatorios con probabilidades.
- Sistema de puntajes.
- Múltiples rondas.
- Interfaz visual estilo arcade.
- Manejo de errores.
- Juego interactivo.


---

# Probabilidades de cofres

- Común -> 60%
- Raro -> 30%
- Legendario -> 10%


---

# Ejemplo de ejecución

>> CAZADOR DE CONTRASEÑAS <<

Ingrese la longitud de la contraseña: 12

Contraseña generada: A7$xLm!9Qw#P

Cofre obtenido:
[★] ¡INCREÍBLE! Has desbloqueado un cofre legendario.

Puntos obtenidos: 50


---

# Posibles mejoras futuras

- Guardado de partidas.
- Ranking de jugadores.
- Música y sonidos.
- Interfaz gráfica.
- Base de datos.
- Niveles de dificultad.


---

# Autor:

Proyecto desarrollado por:
**Salomé Londoño M.**

Institución:
Universidad Nacional Abierta y a Distancia

Programa: 
Ingeniería de Sistemas

Asignatura:
Programación

Fecha:
26 de mayo de 2026.


