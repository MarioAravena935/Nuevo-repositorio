# Crear una lista para almacenar los resultados de la tabla de multiplicar del 5
tabla_multiplicar_5 = []
 
# Calcular la tabla de multiplicar del 5 del 1 al 10
for i in range(1, 11):
    resultado = 5 * i
    tabla_multiplicar_5.append(resultado)
 
# Imprimir la tabla de multiplicar del 5
print("Tabla de multiplicar del 5:")
for i in range(1, 11):
    print(f"5 x {i} = {tabla_multiplicar_5[i-1]}")
