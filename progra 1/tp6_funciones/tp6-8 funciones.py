#actividad 8

def calcular_imc(peso, altura):
    return peso / altura ** 2

peso   = float(input("Ingresá tu peso (kg): "))
altura = float(input("Ingresá tu altura (m): "))
print(f"IMC: {calcular_imc(peso, altura):.2f}")