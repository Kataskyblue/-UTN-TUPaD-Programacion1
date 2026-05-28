# 7. actividad
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma} | Resta: {resta} | Multiplicación: {mult} | División: {div:.2f}")
