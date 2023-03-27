def es_palindromo(palabra):
    # Eliminamos los espacios en blanco y convertimos todo a minúsculas
    palabra = palabra.replace(" ", "").lower()
    # Comparamos la palabra original con su versión invertida
    return palabra == palabra[::-1]

a = input("Ingrese una palabra: ")
print(es_palindromo(a))
