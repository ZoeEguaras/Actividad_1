import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Inicializar el número de fallos 
total_failures = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []

# El usuario elige la dificultad
while True:
    print("Elige una dificultad:")
    print("1. Fácil")
    print("2. Media")
    print("3. Difícil")
    option = input()
    
    # El bucle se rompe SOLO si se ingresa un número válido
    if option in ['1', '2', '3']:
        option = int(option)
        break
    else:
        print("Opción no válida. Intente de nuevo.")

match option:
    case 1:
        # Revelar las vocales
        word_displayed = ""
        for letter in secret_word:
            if letter in "aeiou":
                word_displayed += letter
                guessed_letters.append(letter)
            else:
                word_displayed += "_"
    case 2:
        # Revelar la primera y la úiltima letra (con todas sus ocurrencias)
        word_displayed = ""
        for letter in secret_word:
            if letter in (secret_word[0], secret_word[-1]):
                word_displayed += letter
                guessed_letters.append(letter)
            else:
                word_displayed += "_"
    case 3:
        # No revelar nada
        word_displayed = "_" * len(secret_word)

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while total_failures < 10:
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Esa letra ya fue revelada. Intenta con otra.")
         continue
     # Verificar si el usuario ingresó un caracter correcto
     if not letter.isalpha():
         print("No has ingresado una letra. Inténtalo de nuevo.")
         continue
     # EXTRA: Verificar si el usuario ingresó más de una letra
     if len(letter) != 1:
         print("Has ingresado más de una letra. Intenta ingresando solo una.")
         continue
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta o penalizar al jugador
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         total_failures += 1
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
         break
else:
     print(f"¡Oh no! Has cometido demasiados fallos ({total_failures}).")
     print(f"La palabra secreta era: {secret_word}")