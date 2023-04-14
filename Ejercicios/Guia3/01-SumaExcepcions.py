class Sugod:
    def __init__(self):
        while True:
            try:
                suma1 = int(input("Ingrese un numero entero: "))
                suma2 = int(input("Ingrese otro numero entero: "))

                suma = suma1 + suma2

                print("Suma: ", suma)
                
            except ValueError:
                print("Error, este numero no es un entero")

            finally: 
                respuesta = input("¿quieres seguir sumando valores? (s/n): ")
                if respuesta != "s":
                    break
                

suma = Sugod()