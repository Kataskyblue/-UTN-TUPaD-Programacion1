#herramientas = []
herramientas = ["martillo", "clavo"]
existencias = [2, 4]
while True:
    print("1) carga de herramientas")
    print("2) carga de existencias")
    print("3) mostrar inventario")
    print("4) buscar herramienta ")
    print("5) vender herramienta ")
    print("6) mostrar agotados")
    print("7) salir")

    opcion = input("elige una opcion (1/7): ")

    while not opcion.isdigit():
        print("opcion invalida")
        opcion = input("elige una opcion (1/7)")
    opcion = int(opcion)

    if opcion == 1:
        cargas = input("cuantas cargas desea agregar?: ")
        while not cargas.isdigit():
            print("opcion invalida")
            cargas = input("cuantas cargas desea agregar")
        cargas = int(cargas)

        for i in range(cargas):
            herramienta = input(f"herramienta {i+1}: ").strip().lower()

            while herramienta == "" or herramienta in herramientas:
                if herramienta == "":
                    print("opcion vacia")
                else:
                    print("herramienta duplicada")
            herramientas.append(herramienta)

    elif opcion == 2:
        if len(herramientas) == 0:
            print("primero cargue herramientas")
        else:
            print("carga inicial")
            existencias = []

            for i in range(len(herramientas)):
                print(f"heramienta: {herramientas[i]}")
                cantidad = input("ingrese su stock: ")

                while not cantidad.isdigit():
                    print("numero invalido")
                    cantidad = input("ingrese su stock")

                existencias.append(int(cantidad))




