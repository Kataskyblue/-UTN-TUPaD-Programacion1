ventas = [
    [10, 28, 83, 64, 50, 16, 97],
    [84, 92, 14, 110, 152, 13, 74],
    [15, 19, 145, 148, 129, 220, 231],
    [22, 87, 47, 23, 45, 34, 28]
]

print("total vendido por cada producto: ")

totales_productos = []

for i in range(4):
    suma = 0
    for j in range(7):
        suma+=ventas[i][j]

    totales_productos.append(suma)
    print("producto", i + 1, "total:",suma)

print("dia con mayores ventas totales")

mayor_venta = 0
dia_mayor = 0

for i in range(4):
    suma_dia = 0
    for j in range(7):
        suma_dia+=ventas[i][j]

    print("dia", j + 1, "total vendido", suma_dia)

    if suma>mayor_venta:
        mayor_venta = suma_dia
        dia_mayor = j + 1
print("el dua con mas ventas fue el dia", dia_mayor,"con un total de", mayor_venta)

mayor_producto = max(totales_productos)
producto_mas_vandido = totales_productos.index(mayor_producto)+1

print("producto mas vendido en la semana: ")
print("producto",producto_mas_vandido,"con un total de", mayor_producto)
