# Definimos una lista de strings
strings = ['Hola', 'esto', 'es', 'una', 'prueba']

# Abrimos un archivo en modo escritura ('w')
with open('archivo.txt', 'w') as archivo:
    try:
        #strings = input("Ingresa los elementos de la lista separados por espacios o comas: ")

        # Convertimos los elementos a una lista utilizando el método split()
        #lista = strings.split()

        # Tratamos de escribir un entero en el archivo
        archivo.write(123)
    except TypeError:
        # Capturamos la excepción TypeError que se produce cuando se intenta escribir un objeto que no es str en un archivo de texto
        print("Error: no se puede escribir un entero en un archivo de texto")
    else:
        print("La operación se realizó con éxito")