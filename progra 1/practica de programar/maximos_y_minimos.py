#numero maximo

cant_numeros = 4
max_num = float("-inf")

for cont in range(cant_numeros):
    print("ingrese numero",(cont+1))
    num = int(input())
    if num > max_num:
        max_num = num

print("el valor maximo es:", max_num) 

#numero minimo

cant_numeros = 4
min_num = float("inf")

for cont in range(cant_numeros):
    print("ingrese numero",(cont+1))
    num = int(input())
    if num > min_num:
        min_num = num

print("el valor minimo es:", min_num) 

#AMBOS

cant_numeros = 4
max_num = float("-inf")
min_num = float("inf") 
 

for cont in range(cant_numeros):
    print("ingrese numero",(cont+1))
    num = int(input())
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

print("el valor maximo es:", max_num)  
print("el valor minimo es:", min_num) 

#dice la posicion en la que salio

cant_numeros = 4
max_num = num
min_num = num
pos_max = -1
pos_min = -1

print("ingrese numero 1")
num = int(input())
 
for cont in range(1,cant_numeros+1):
    print("ingrese numero",(cont+1))
    num = int(input())
    if num > max_num:
        max_num = num
        pos_max = cont 
    elif num < min_num:
        min_num = num
        pos_min = cont
 
print("el valor maximo es:", max_num, "y salio en la pos",pos_max)  
print("el valor minimo es:", min_num, "y salio en la pos",pos_min)