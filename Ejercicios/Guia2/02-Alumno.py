class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
        
        if self.nota >= 6:
            print(f"El {self.nombre} está regular")
        else:
            print(f"El {self.nombre} no está regular")

nombre1 = input("Ingrese el nombre del primer alumno: ")
nota1 = float(input("Ingrese la nota del primer alumno: "))

nombre2 = input("Ingrese el nombre del segundo alumno: ")
nota2 = float(input("Ingrese la nota del segundo alumno: "))

alumno1 = Alumno(nombre1, nota1)
alumno2 = Alumno(nombre2, nota2)

alumno1.imprimir_datos()
print("--------------------")
alumno2.imprimir_datos()
        