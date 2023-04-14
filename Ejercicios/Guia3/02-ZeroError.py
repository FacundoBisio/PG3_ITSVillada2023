while True:
    try:
        num1 = int(input("Ingrese un numero entero: "))
        num2 = int(input("Ingrese otro numero entero: "))

        division = num1 / num2

        print("Division: ", division)
        
    except ZeroDivisionError:
        print("Error. No se puede dividir por cero")

    finally: 
        respuesta = input("¿quieres seguir dividiendo valores? (s/n): ")
        if respuesta != "s":
            break