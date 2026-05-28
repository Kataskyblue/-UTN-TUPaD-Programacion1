#activida 10 

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))
print(f"Promedio: {calcular_promedio(a, b, c):.2f}")