"""
Ciclo for

sé exactamente cuando voy a parar el ciclo

es ideal para recorrer listas, tuplas, diccionarios, etc (secuencias)
"""

"""
Puedo nombrar una variable:

* No use caracteres especiales
* No empiece por un número
* No contenga espacios

* Si puede tener un número en el medio o al final
* Puede tener _ (guión bajo)
* Puede tener mayúsculas y minúsculas

Camel

nombreEstudiante


Por guiones

nombre_estudiante
"""

lista = ["Dinosaurio", 23, True, 45.5, "Amazon"]


# for [variable_de_iteración] in lista:
for x in lista:
    print(f"Elemento {x} tipo de dato {type(x)}")
    

##### EJERCICIO ########
# Dada la siguiente lista imprime SOLO los números pares
numeros = [2, 45, 19, 13, 178]


numeros = [2, 45, 19, 13, 178]

for x in numeros:
    if x > 10:  
        print(x)
