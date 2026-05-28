#ejercicio 10
ventas = [
    [10, 5, 8, 3, 7, 9, 4],
    [6, 2, 11, 8, 5, 3, 7],
    [3, 9, 4, 6, 10, 2, 8],
    [7, 4, 6, 9, 3, 8, 5]
]

# PARTE 1: total por producto
producto = 0
for fila in ventas:
    producto += 1
    total = sum(fila)
    print(f"producto {producto}: {total} unidades")

# PARTE 2: dia con mas ventas
mayor_venta = 0
dia_mayor = 0
for i in range(7):
    total_dia = 0
    for fila in ventas:
        total_dia += fila[i]
    if total_dia > mayor_venta:
        mayor_venta = total_dia
        dia_mayor = i + 1
print(f"dia con mas ventas: dia {dia_mayor} con {mayor_venta} unidades")

mayor_total = 0
producto_mayor = 0
producto = 0
for fila in ventas:
    producto += 1
    total = sum(fila)
    if total > mayor_total:
        mayor_total = total
        producto_mayor = producto

print(f"producto mas vendido: producto {producto_mayor} con {mayor_total} unidades")