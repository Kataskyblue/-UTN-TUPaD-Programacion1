#actividad 1

notas =[5, 4, 6, 8, 9, 10, 3, 7, 2 ,1]

print("lista de notas", notas)

promedio = sum(notas) /len(notas)
print("el promedio de notas: ", promedio)

nota_max = max(notas)
notas_min = min(notas)

print("la nota mas alta fue: ",nota_max)
print("la nota mas baja fue:",notas_min)

#actividad 2

productos = []

for i in range(5):
    producto = input("Ingrese un producto: ")
    productos.append(producto)


print("Lista actualizada: ")
print(sorted(productos))


eliminar = input("que producto desea eliminar?: ")

if eliminar in productos:
    productos.remove(eliminar)

print("lista actualizada")
print(productos)

#actividad 3

import random
numero_secreto = [random.randint(1,100) for i in range(15)]

pares = []
impares = []

for num in numero_secreto:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista de pares:", pares)
print("Lista de impares:", impares)

print("cantidad de pares: ", len(pares))
print("cantidad de pares: ", len(impares))

#actividad 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_sin_repetirse = list(set(datos))

print ("lista sin repetidos: ", datos_sin_repetirse) 

#actividad 5

lista_estudiantes_presentes = ["mads mikkelsen ", "león kennedy", "henry cavill", "ash williams", "bruce campbell", "ricardo iorio", "ricardo fort", "jason voorhees"]

elegir = input("agregara o quitara un estudiante?:")
if elegir == "agregar":
    agregar = lista_estudiantes_presentes.append(input( "que estudiante desea agregar?: "))
    print(lista_estudiantes_presentes)
elif elegir == "quitar":
    quitar = lista_estudiantes_presentes.remove(input("que estudiante eliminara?: "))
    print(lista_estudiantes_presentes)

#actividad 6

lista = [22, 34, 5, 6, 7, 9, 8]
lista.reverse()

print(lista)

#actividad 7

temperaturas = [
    [10, 32],
    [-3, 12],
    [15, -6],
    [27, 8],
    [-9, 10],
    [32, 12],
    [13, -4]
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

#actividad 8

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

#actividad 9

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def mostrar_tablero(tablero):
    print("\nTABLERO:")
    for fila in tablero:
        print(" ".join(fila))
    print()

mostrar_tablero(tablero)

for turno in range(9):
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "0"

    print("turno del jugador", jugador)

    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))

    if tablero[fila][columna]== "_":
        tablero[fila][columna]= jugador
    else:
        print("casilla ocupada, pierdes el turno")
        continue

    mostrar_tablero(tablero)

#actividad 10

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
