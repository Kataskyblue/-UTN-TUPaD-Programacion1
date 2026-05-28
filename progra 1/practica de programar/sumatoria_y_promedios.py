cant_numeros = 5
sumatoria = 0

for cont in range(1,cant_numeros+1):
    print("ingrese numero",cont)
    num = int(input())
    sumatoria += num
    print()

print("la sumatoria de los valores es: ",sumatoria)
print("el valor promedio es: ",sumatoria/cant_numeros) 