notas = [
    [10, 6, 3],
    [4, 8, 6],
    [7, 8, 9],
    [10, 1, 7],
    [1, 9, 5]
]

print("promedio de cada estudiante:")

for i in range(5):
    suma = 0
    for j in range(3):
        suma+=notas[i][j]
    promedio = suma / 3

    promedio=suma / 3
    print("estudiante",i + 1,"promedio", promedio)
