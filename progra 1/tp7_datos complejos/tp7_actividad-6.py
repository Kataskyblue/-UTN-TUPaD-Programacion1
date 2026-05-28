alumnos = {}

for i in range(3):

    nombre = input("ingrese eol nombre del alumno: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    alumnos[nombre] = (nota1, nota2, nota3)

print("\nPromedios:")

for nombre, notas in alumnos.items():

    promedio = sum(notas) / len(notas)

    print(nombre, "tiene promedio:", promedio)

    