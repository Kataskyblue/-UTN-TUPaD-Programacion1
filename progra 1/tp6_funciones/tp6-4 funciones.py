#actividad 4

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2  
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio      
radio = input("ingrese el radio: ")
while not radio.isdigit():
    print("ingrese un numero valido")
    radio = input("ingrese el radio: ")
radio = int(radio)

print(f"area: {calcular_area_circulo(radio):.2f}")
print(f"perimetro: {calcular_perimetro_circulo(radio):.2f}")