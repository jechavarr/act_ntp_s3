total = 0

while True:
    n = input ("Numero (0 para salir): ")
    if n == "0":
        break
    total += int (n)

print ("Total: ", total)