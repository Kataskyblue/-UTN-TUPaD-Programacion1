import turtle
import time

# Configuración de pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Te amo mamá ❤️")

# Configuración del dibujo
corazon = turtle.Turtle()
corazon.speed(0)
corazon.speed(0)
corazon.color("red")
corazon.pensize(3)

# Función para dibujar un corazón
def dibujar_corazon(tamaño):
    corazon.penup()
    corazon.goto(0, -tamaño)
    corazon.pendown()
    corazon.begin_fill()

    corazon.left(140)
    corazon.forward(tamaño * 2)

    corazon.circle(-tamaño, 200)

    corazon.left(120)
    corazon.circle(-tamaño, 200)

    corazon.forward(tamaño * 2)

    corazon.end_fill()
    corazon.setheading(0)

# Función de animación (latido)
def animacion():
    while True:
        corazon.clear()
        dibujar_corazon(80)
        time.sleep(0.4)

        corazon.clear()
        dibujar_corazon(90)
        time.sleep(0.4)

# Texto "Te amo mamá"
texto = turtle.Turtle()
texto.hideturtle()
texto.color("white")
texto.penup()
texto.goto(0, -180)
texto.write("Te amo mamá ❤️", align="center", font=("Arial", 24, "bold"))

# Ejecutar animación
animacion()

turtle.done()
