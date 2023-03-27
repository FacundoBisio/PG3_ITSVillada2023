def ordenar_lista(lista):
    return sorted(lista, reverse=True)

lista = []  # crear una lista vacía

while True:
    valor = input("Ingrese un valor para agregar a la lista o 'fin' para terminar: ")
    if valor == 'fin':
        break  # salir del bucle si el usuario ingresa 'fin'
    lista.append(int(valor))  # agregar el valor a la lista (se convierte a un entero antes de agregarlo)

print("La lista ingresada es:", lista)

lista_ordenada = ordenar_lista(lista)
print(lista_ordenada)