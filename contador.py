contador = 0

while True:
    print(contador)
    detener = input("Escriba algo si desea detenerse, de caso contrario presione Enter: ")
    
    if detener != "":
        print("Detenido en:", contador)
        break
    
    contador += 1