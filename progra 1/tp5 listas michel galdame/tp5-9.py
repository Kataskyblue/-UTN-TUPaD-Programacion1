# ejercicio 9

tablero = [
    # 1    #2   #3
    ["-", "-", "-"],#1
    ["-", "-", "-"],#2
    ["-", "-", "-"] #3
]
turno = "X"
while True:
    for fila in tablero:
        print(fila[0], fila[1], fila[2])

    fila = int(input("ingrese fila (1-3): ")) -1
    columna = int(input("ingrese columna (1-3): ")) -1
    if fila <0 or fila >= len(tablero): 
        print("fila invalida")
        continue
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = turno

    if turno == "X":
        turno = "O"
    else:
        turno = "X"

    print(f"turno del jugador {turno}")


