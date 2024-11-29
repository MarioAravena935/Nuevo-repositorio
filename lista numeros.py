numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mayor = 0  # Declarar una variable inicial (número, no lista)

for numero in numeros:  # Cambiar la variable del bucle a singular
    if numero > mayor:
        mayor = numero  # Actualizar el valor de 'mayor' si se encuentra un número mayor

print("El número mayor es:", mayor)  # Imprimir el mayor fuera del bucle
