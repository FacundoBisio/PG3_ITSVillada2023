def contar_vocales(frase):
    # Convertimos todo a minúsculas para evitar problemas con mayúsculas y minúsculas
    frase = frase.lower()
    # Definimos una lista con todas las vocales
    vocales = ['a', 'e', 'i', 'o', 'u']
    # Inicializamos un contador de vocales en 0
    contador = 0
    # Recorremos cada caracter de la frase
    for caracter in frase:
        # Si el caracter es una vocal, aumentamos el contador en 1
        if caracter in vocales:
            contador += 1
    # Devolvemos el valor del contador
    return contador

a = input("Ingrese una frase: ")
print(contar_vocales(a))