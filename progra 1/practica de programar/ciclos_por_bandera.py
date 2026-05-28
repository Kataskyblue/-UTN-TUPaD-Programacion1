umbral = 10
sumatoria = 0
cont = 0


while sumatoria < umbral :
    cont += 1
    print("ingrese un numero: ",cont)
    num = int(input())
    sumatoria += num
    
print("el promedio de valores leidos es",sumatoria/cont)
