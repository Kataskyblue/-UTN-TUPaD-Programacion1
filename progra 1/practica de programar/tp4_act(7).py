temperaturas = [
    [10, 2],
    [  3, 10],
    [5, 6],
    [7, 8],
    [9, 10],
    [3, 6],
    [9, 4]
]

suma_min = 0
suma_max = 0

for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]

promedio_min = suma_min/7
promedio_max = suma_max/7

mayor_amplitud = 0
dia_mayor = 0   

for i in range(7):
    minima = temperaturas[i][0]
    maximo = temperaturas[i][1]

    amplitud = maximo - minima

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i + 1

print("Mayor amplitud térmica:", mayor_amplitud)
print("Se registró en el día:", dia_mayor)   