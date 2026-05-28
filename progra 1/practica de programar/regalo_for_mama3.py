import math
from turtle import *

# Fórmula matemática del corazón
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

# Configuración
speed(0)
bgcolor("black")
color("red")
pensize(1)

# Dibujar efecto de rayos
for i in range(0, 6000):
    k = i / 100

    x = hearta(k) * 20
    y = heartb(k) * 20

    penup()
    goto(0, 0)       # siempre vuelve al centro
    pendown()
    goto(x, y)       # línea hacia el borde del corazón

# Texto debajo
penup()
goto(0, -280)
color("white")
write("Te amo mamá ❤️", align="center", font=("Arial", 28, "bold"))

hideturtle()
done()