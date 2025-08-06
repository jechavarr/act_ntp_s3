import random

secreto = random.randint(1, 10)
adivina = 0

while adivina != secreto:
    adivina = int(input("Adivina el número (del 1 al 10): "))
    if adivina != secreto:
        print("No es ese, intenta de nuevo.")

print("¡Bien hecho! Adivinaste el número.")