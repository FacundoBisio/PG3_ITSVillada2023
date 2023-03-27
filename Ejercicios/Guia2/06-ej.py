class Familia:
    def __init__(self, nomp, nomm, nomh):
        self.padre = nomp
        self.madre = nomm
        self.hijos = nomh
    
    def __str__(self):
        return f"""
        Padre:{self.padre} 

        Madre: {self.madre}

        Hijos: {" ".join(self.hijos)}
        """

nomp = input("Ingrese nombre del padre: ")
nomm = input("Ingrese nombre de la madre: ")
hijos = []

for _ in range (3):
    hijos.append(input("Ingrese hijo: "))

familia = Familia(nomp, nomm, hijos)
print(familia)