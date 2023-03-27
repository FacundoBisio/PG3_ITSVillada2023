class Operaciones:
    def __init__(self):
        self.num1 = int(input("Ingrese un numero entero: "))
        self.num2 = int(input("Ingrese otro numero entero: "))
        
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