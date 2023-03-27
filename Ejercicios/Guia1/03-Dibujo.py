ancho = int(input("Ingrese el ancho del rectángulo: "))
alto = int(input("Ingrese el alto del rectángulo: "))
caracter = input("Ingrese el caracter a utilizar en el dibujo: ")

for i in range(alto):
    for j in range(ancho):
        print(caracter, end="")
    print()