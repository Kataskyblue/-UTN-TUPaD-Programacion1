#ejercicio 1

herramientas = []
existencias = []

for i in range(5):
    herramienta = input(f"ingrese herramientas{i+1}: ").strip().lower()

    while herramienta == "" or herramienta in herramientas:
        if herramienta == "":
            print("nombre vacio")
        else:
            print("herramienta duplicada")

        herramienta = input(f"ingrese herramienta {i+1}: ").strip().lower()

    herramientas.append(herramienta)

for i in range(len(herramientas)):
    print(f"herramienta : {herramientas[i]}")
    cantidad = input ("ingrese stock: ")

    while not cantidad.isdigit():
        print("ingrese un numero valido")
        cantidad = input("ingrese stock: ")
    existencias.append(int(cantidad))

print("\nInventario:")
for i in range(len(herramientas)):
    print(f"{herramientas[i]}: {existencias[i]} unidades")
