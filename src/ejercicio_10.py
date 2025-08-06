contador = 0 

while True:
    palabra = input ("Escribe una palabra ('Fin' para salir)")
    if palabra == 'Fin':
        break
    contador += 1
print (f"Se leyeron {contador} palabras")