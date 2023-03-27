class Persona:
    def __init__(self, nombre):
        while not self.validar_nombre(nombre):
            nombre = input("El nombre debe contener solo letras. Ingresa el nombre de nuevo: ")
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print("Mi nombre es", self.nombre)
    
    def validar_nombre(self, nombre):
        if not nombre.isalpha() or nombre.isnumeric():
            return False
        return True
            
# Crear objetos de la clase Persona
nombre1 = input("Ingresa el nombre de una persona: ")
persona1 = Persona(nombre1)

nombre2 = input("Ingresa el nombre de la otra persona: ")
persona2 = Persona(nombre2)

# Mostrar nombres de las personas
persona1.mostrar_nombre()
persona2.mostrar_nombre()