"""

Lista

Una coleccion ordenada de elementos
Cualquier tipo de datos puede ser un elemento
mutable
usamos parentesis cuadrados [] y separamos los elementos

"""
# Definición de la lista
myFruitList = ["Pera", "banana", "mango"]

# Mostrar la lista completa
print(myFruitList)  # ['Pera', 'banana', 'mango']

# Verificar el tipo de datos
print(type(myFruitList))  # <class 'list'>

# Acceder y mostrar cada elemento de la lista
# Definición de la lista
myFruitList = ["Pera", "banana", "mango"]

print(myFruitList[0])  # Pera
print(myFruitList[1])  # banana
print(myFruitList[2])  # mango


### metodos de las listas


## .append() agregar un elemento en la lista

# añadir tomate

myFruitList.append("Tomate")
print(myFruitList)

## remover
myFruitList.remove("banana")

print(myFruitList)

"""

Tupla

es una coleccion INMUTABLE ordenada de elementor

ES UNA LISTA QUE NO PUEDE CAMBIAR
acepta repetidos
usamos parentesis redondos () y separamos 
"""

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

## acceder a un elemento por posición

print(myFinalAnswerTuple[0])

print(myFinalAnswerTuple[1])

print(myFinalAnswerTuple[2])


"""

Diccionario

es una coleccion ordenada de elementos clave valor

clave : entero o string, es unica

valor : cualquier tipo de datos


"""

fondosRestart = {
  "Mario": "Amarillo",
  "Luna": "Naranjo",
  "Jorge": "Negro",
  "Matias": "Blanco"
}

print(fondosRestart)
print(type(fondosRestart))

if "Gustavo" not in fondosRestart:
    fondosRestart["Gustavo"] = "gris"

print(fondosRestart["Gustavo"])
