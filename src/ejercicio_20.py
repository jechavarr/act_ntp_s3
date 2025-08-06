edad = 0
mayor = 0

while edad != -1:
    edad = int(input("Ingresa una edad (-1 para terminar): "))
    if edad > mayor and edad != -1:
        mayor = edad

print("La edad mayor ingresada fue:", mayor)