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

    