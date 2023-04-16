while True:
    try:
        num1 = float(input("Ingrese un numero entero: "))
        num2 = float(input("Ingrese otro numero entero: "))

        division = num1 / num2

        print("Division: ", division)
        
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")

    except ValueError:
        print("Error: no se puede ingresar strings")

    finally: 
        respuesta = input("¿quieres seguir dividiendo valores? (s/n): ")
        if respuesta != "s":
            break