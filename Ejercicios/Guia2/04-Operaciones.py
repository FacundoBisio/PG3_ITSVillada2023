class Operaciones:
    def __init__(self):
        while True:
            try:
                self.num1 = int(input("Ingrese un numero entero: "))
                
                break
            except ValueError:
                print("Error, este numero no es un entero")
                
        while True:
            try:
                self.num2 = int(input("Ingrese otro numero entero: "))
                break
            except ValueError:
                print("Error, este numero no es un entero")
        
        
    def operaciones(self):
        print(f"Suma: {self.num1 + self.num2}")
        print(f"Resta: {self.num1 - self.num2}")
        if self.num2 != 0:
            print(f"Division: {self.num1 / self.num2}")
        else:
            print("Division: No se puede didvir por 0")
        print(f"Multiplicacion: {self.num1 * self.num2}")

op = Operaciones()
op.operaciones()