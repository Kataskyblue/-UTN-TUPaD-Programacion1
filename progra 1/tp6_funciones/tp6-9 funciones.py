#actividad 9

def celsius_a_fahrenheit (celsius):
    return celsius * 9/5 + 32

celsius = float(input("Ingresá la temperatura en Celsius: "))
print(f"Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")
