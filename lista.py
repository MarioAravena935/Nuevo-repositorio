# Definir una lista con números
lista = [4, 3, 7, 1, 100, 5]

# Inicializar la variable mayor con un valor bajo
mayor = 0

# Recorrer cada número en la lista
for numero in lista:
    if mayor < numero:
        mayor = numero

# Imprimir el número mayor
print("El mayor número es:", mayor)
