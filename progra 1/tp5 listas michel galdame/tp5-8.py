#ejercicio 8

estudiantes = [
    [4, 7, 2],
    [9, 1, 5],
    [3, 10, 6],
    [8, 2, 7],
    [1, 9, 4]
]

alumno = 0

for materias in estudiantes :
    alumno += 1
    promedio = sum(materias) / len(materias)
   
    print(f"promedio estudiant {alumno}: {promedio:.2f}")

print()

for i in range(3):
    suma = 0
    for estudiante in estudiantes:
        suma += estudiante [i]
    promedio = suma / len(estudiantes)
    print(f"promedio materia {i+1}: {promedio:.2f}")

