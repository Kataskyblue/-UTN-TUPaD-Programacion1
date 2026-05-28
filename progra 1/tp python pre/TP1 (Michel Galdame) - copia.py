#actividad 1

print("hola mundo")

#actividad 2

nombre = input("porfavor, ingrese su nombre:")

print("mucho gusto," + nombre + "!")

#actividad 3

nombre = input("porfavor, ingrese su nombre:")

apellido = input("¿cual es tu apellido?: ")

edad = input("¿cuantos años tienes?: ")

pais = input ("¿de que pais vienes?: ")

print("me llamo " + nombre + " mi apellido es " + apellido + " tengo " + edad + " años" + " soy de " + pais)

#actividad 4

radio = 6
pi = 3.3050
area = pi * radio * radio

print("el area del circulo es:", area)


#actividad 5

#convertir segundos ahoras

segundos_input = input("ingresa la cantidad de segundos: ")

segundos = float(segundos_input)

horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.4f} horas.") 
print(f"redondeando:{segundos} segundos ≈ {horas:.2f} horas.")

#actividad 6

numero = int(input("introduzca un numero porfavor:"))

for i in range(0, 11):
 resultado = i * numero
 print(numero, " x ", i, " = ", resultado)

 #actividad 7

 print("ingrese el primer numero: ")
n1 = float(input())
print("ingrese el segundo numero: ")
n2 = float(input())
suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2
print("la suma es: ",suma)
print("la resta es: ",resta)
print("la multiplicacion: ",mult)
print("la division es: ",div)

#actividad 8

def calcularIMC( p, a):
    return p / (a * a)

def NivelDePeso(IMC):
    if IMC < 18.5:
        return "Bajo peso"
    elif 18.5 <= IMC <= 24.9:
        return "normal"
    elif 25 <= IMC <= 29.9:
        return "sobre peso "
    elif 30 <= IMC <= 34.9:
        return "obesidad 1"
    elif 35 <= IMC <= 39.9:
        return "obesidad 2 "
    elif 40 <= IMC <= 49.9:
        return "obesidad 3 "
    elif 50 <= IMC <= 50:
        return "obesidad 4 "


peso = float(input("ingrese el peso(kg): "))
altura = float(input("ingrese la altura(m): "))
print ("su nivel de peso es: ", NivelDePeso(calcularIMC(peso, altura)))

#actividad 9

c = float(input("ingrese la cantidad de grados  celsius a convertir: "))
f = 9 / 5 * c + 32
print(c, " grados celsius esquvale a ",f, " grados Fafrenheit")

#actividad 10

num1 = float(input("ingresa el primer numero:"))
num2 = float(input("ingresa el segundo numero:"))
num3 = float(input("ingresa el tercer numero:"))

promedio = (num1 + num2 + num2)/3

print("el promedio es:", promedio)