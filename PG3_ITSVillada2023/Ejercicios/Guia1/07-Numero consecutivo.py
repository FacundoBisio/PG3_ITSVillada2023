def es_step(numero):
    # Convertir el número a una cadena de caracteres
    numero_str = str(numero)
    
    # Recorrer cada dígito del número
    for i in range(len(numero_str) - 1):
        # Calcular la diferencia entre el dígito actual y el siguiente
        diferencia = abs(int(numero_str[i]) - int(numero_str[i+1]))
        
        # Si la diferencia no es 1, el número no es "step"
        if diferencia != 1:
            return False
    
    # Si se recorrieron todos los dígitos sin encontrar diferencias distintas de 1, el número es "step"
    return True

num = input("ingrese un numero para calcular si es step o no: ")
print(es_step(num))