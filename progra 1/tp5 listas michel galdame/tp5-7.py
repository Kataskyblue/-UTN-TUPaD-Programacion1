#ejercicio 7

temperatura = [
    [12, 20],
    [13, 40],
    [5, 26],
    [17, 38],
    [9, 10],
    [11, 42],
    [15, 24]
]

suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia_mayor = 0
dia_actual = 0

for dia in temperatura:
    dia_actual += 1
    minima = dia[0]
    maxima = dia[1]
    suma_minimas += minima
    suma_maximas += maxima
    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = dia_actual


promedio_minima = suma_minimas / len(temperatura)
promedio_maximo = suma_maximas / len(temperatura)

print(f"promedio minimas: {promedio_minima:.2f}")
print(f"promedio maximas: {promedio_maximo:.2f}")
print(f"el dia con mayor temperatura es: {dia_mayor}")
 

