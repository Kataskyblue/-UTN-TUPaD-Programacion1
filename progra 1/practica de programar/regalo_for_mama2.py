import math
from turtle import *

# Fórmulas matemáticas para el corazón
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Configuración de Turtle
speed(0)
bgcolor("black")
color("red")

penup()

# Dibujar el corazón
for i in range(0, 6000):
    k = i / 100
    x = hearta(k) * 20
    y = heartb(k) * 20
    goto(x, y)
    pendown()

# Mensaje debajo del corazón
penup()
goto(0, -250)
color("white")
write("Te amo mamá ❤️", align="center", font=("Arial", 28, "bold"))

hideturtle()
done()
