class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def lado_mayor(self):
        mayor = self.lado1
        if self.lado2 > mayor:
            mayor = self.lado2
        if self.lado3 > mayor:
            mayor = self.lado3
        return mayor
    
    def es_equilatero(self):
        return self.lado1 == self.lado2 and self.lado1 == self.lado3
    
# Ejemplo de uso del programa
lado1 = input("Inrese lado 1: ")
lado2 = input("Inrese lado 2: ")
lado3 = input("Inrese lado 3: ")


triangulo1 = Triangulo(lado1, lado2, lado3)
print("Lado mayor:", triangulo1.lado_mayor())
if triangulo1.es_equilatero():
    print("El triángulo es equilátero.")
else:
    print("El triángulo no es equilátero.")