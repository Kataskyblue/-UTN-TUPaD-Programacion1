#tp integrador ejercicio 1


nombre_cliente = input("ingrese su nombre porfavor: ")
while not nombre_cliente.isalpha():
    print("ingrese un nombre valido")
    nombre_cliente = input("ingrese su nombre: ")

cantidad_productos = input(" que cantidad de productos desea comprar: ")
while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("ingrese un nombre valido")
    cantidad_productos= input("que cantidad de productos desea comprar: ")
cantidad_productos = int(cantidad_productos)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(cantidad_productos):
    print(f"\nproducto {i + 1}")
    precio = input("ingrese el precio: ")
    while not precio.isdigit():
        print("ingrese un numero valido")
        precio = input("ingrese el precio: ")
    precio = int(precio)
    
    while precio <= 0:
        print("ingrese un precio superior a 0 ")
        precio = int(input("ingrese el precio: "))

    total_sin_descuento += precio

    descuento = input("tiene algun descuento? S/N: ").lower()

    while descuento != "s" and descuento != "n":
        print("ingrese S o N!!")
        descuento = input("tiene descuento? (S/N): ").lower()

    if descuento == "s":
        precio_final = precio - (precio * 0.10)
        print(f" su precio seria de {precio_final}")
        total_con_descuento += precio_final
    else:
        print(f"su precio seria de {precio}")
        total_con_descuento += precio
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos
print("\n=========================================")
print(f"cliente {nombre_cliente}")
print (f"cantidad de productos: {cantidad_productos}")
print(f"total sin descuentos ${total_sin_descuento}")
print(f"total con descuentos ${total_con_descuento}")
print(f"ahorro: {ahorro}")
print(f"promedio del producto: ${promedio:.2f}")
