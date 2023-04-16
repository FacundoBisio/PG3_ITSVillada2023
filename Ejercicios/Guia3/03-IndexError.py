meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

while True:
    try:
        num_mes = int(input("Ingresa un número de mes (1-12): "))
        # Si el número está dentro del rango de 1 a 12, mostramos el nombre del mes correspondiente
        if num_mes >= 1 and num_mes <= 12:
            nombre_mes = meses[num_mes - 1]
            print("El mes correspondiente al número", num_mes, "es", nombre_mes)
        else:
            print("Error: el número debe estar entre 1 y 12")

    # Capturamos la excepción IndexError, que se produce si el usuario ingresa un número fuera del rango de la tupla
    except IndexError:
        print("Error: el número debe estar entre 1 y 12")

    # Capturamos la excepción ValueError, que se produce si el usuario ingresa algo que no es un número entero
    except ValueError:
        print("Error: debes ingresar un número entero")

    finally: 
            respuesta = input("¿Quieres seguir numeros de mes? (s/n): ")
            if respuesta != "s":
                break
