nombre = input("Escribe un nombre: ").lower()
vocales = "aeiou"
contador = 0
 
for letra in nombre:
    if letra in vocales:
        contador += 1
 
print(f"El nombre ingresado tiene un total de {contador} vocales")