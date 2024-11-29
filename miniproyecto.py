opcion = 0  # Inicializamos la opción con un valor entero, no con una cadena vacía.

while opcion != 6:  # El bucle continuará hasta que se elija la opción 6.
    print("Bienvenido, las opciones son: ")
    print("1. Crear un libro")
    print("2. Actualizar un libro")
    print("3. Eliminar un libro")
    print("4. Consultar un libro")
    print("5. Mostrar todo el inventario")
    print("6. Salir")

    # Pedimos la opción al usuario.
    opcion = int(input("Ingresa una opción que quieras hacer: "))

    # Comprobamos la opción ingresada.
    if opcion == 1:
        print("Vamo a crear")
    elif opcion == 2:
        print("Vamo a actualizar")
    elif opcion == 3:
        print("Vamo a eliminar")
    elif opcion == 4:
        print("Vamo a consultar")
    elif opcion == 5:
        print("Vamo a mostrar")
    elif opcion == 6:
        print("Hasta pronto")
    else:
        print("Ingresa una opción válida")

