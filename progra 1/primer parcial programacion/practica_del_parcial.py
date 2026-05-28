productos = ["monitor", "mouse", "teclado", "microfono", "camara", "audifonos"]
precios =  [200, 15, 25, 5, 40, 80]

#A) nombre del producto con menor precio
minimo = min(precios)
pos = precios.index(minimo)
produc = productos[pos]
print(produc)
#B) precio de un mouse
posPRO = productos.index["mouse"]
precio = precios[posPRO]
print(precio)
#C) presentar un top 5 de productos en orden de mayor a menor segun su precio, ejemplo:
i = 0 
while i < 5:
    maxi= max(precios)
    posMAx = precios.index(max)
    nombre= productos[posMAx]
    print(nombre, maxi)
    del productos[posMAx]
    del precios[posMAx]
    i+=1