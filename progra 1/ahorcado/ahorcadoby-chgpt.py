import random

# ---------------------------
# Lista de palabras
# ---------------------------
palabras = ["python", "computadora", "programacion", "teclado", "internet"]


# ---------------------------
# Función para elegir palabra
# ---------------------------
def elegir_palabra(lista):
    return random.choice(lista)


# ---------------------------
# Función para mostrar estado
# ---------------------------
def mostrar_estado(estado, intentos):
    print("\nPalabra:", " ".join(estado))
    print("Intentos restantes:", intentos)


# ---------------------------
# Función para pedir letra
# ---------------------------
def pedir_letra():
    letra = input("Ingresa una letra: ").lower()
    return letra


# ---------------------------
# Función para actualizar palabra
# ---------------------------
def actualizar_estado(palabra, estado, letra):
    acierto = False

    for i in range(len(palabra)):
        if palabra[i] == letra:
            estado[i] = letra
            acierto = True

    return acierto


# ---------------------------
# Función principal del juego
# ---------------------------
def jugar():
    palabra_secreta = elegir_palabra(palabras)
    estado = ["_"] * len(palabra_secreta)
    intentos = 6

    print("🎮 Bienvenido al juego del Ahorcado")

    while intentos > 0:
        mostrar_estado(estado, intentos)

        letra = pedir_letra()

        # Validación básica
        if len(letra) != 1 or not letra.isalpha():
            print("⚠️ Ingresa solo UNA letra válida")
            continue

        if letra in estado:
            print("⚠️ Ya adivinaste esa letra")
            continue

        # Verificar letra
        if actualizar_estado(palabra_secreta, estado, letra):
            print("✅ Adivinaste una letra correctamente")
        else:
            intentos -= 1
            print("❌ Letra incorrecta, te quedan", intentos, "intentos")

        # Verificar victoria
        if "_" not in estado:
            print("\n🎉 ¡Ganaste! La palabra era:", palabra_secreta)
            return

    # Si pierde
    print("\n💀 Perdiste. La palabra era:", palabra_secreta)


# ---------------------------
# Ejecutar juego
# ---------------------------
jugar()