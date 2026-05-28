EDAD_MINIMA = 18
cant_personas = int(input("ingrese una cantidad de personas: "))
cant_personas_mayores = 0

for cont in range(cant_personas):
    print("ingrese la edad", (cont+1))
    edad = int(input())
    if edad >= EDAD_MINIMA:
        cant_personas_mayores += 1
porc = (cant_personas_mayores/ cant_personas) * 100
print("el porventajde de personas mayores de edad es",porc)