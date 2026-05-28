inicio = int(input("ingrese el primer valor: "))
fin = int(input("ingrese el segundo valor: "))

if inicio > fin:
    inicio, fin = fin, inicio

suma =0

for i in range(inicio + 1, fin):
    suma += i

print("la suma de los numeros es: ",suma)
