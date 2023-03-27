class Persona:
    def __init__(self ,nom, ape):
        self.nombre = nom
        self.apellido = ape



class Empleado(Persona):
    def __init__(self, nom, ape):
        super().__init__(nom, ape)

    def sueldo(self, suel):
        self.suel = suel
        if self.suel >= 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
sueldo = int(input("Ingrese su sueldo: "))

em =Empleado(nombre, apellido)
em.sueldo(sueldo)
