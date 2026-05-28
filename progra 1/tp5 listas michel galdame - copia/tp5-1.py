#ejercicio 1

notas = [10, 4, 7, 3, 9, 6, 2, 9, 8, 1]

print("notas de estudiantes: ", end="")
for nota in notas:
    print(nota, end=" ")
print()

promedio = sum(notas) / len(notas) 
print (f"pormedio de los estudiantes: {promedio}")
print (f"la nota mas alta fue: {max(notas)}")
print (f"la nota mas baja fue: {min(notas)}")