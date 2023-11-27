class Chica:
    def __init__(self,nombre,edad,apellido):
        self.nombre =nombre
        self.edad =edad
        self.apellido =apellido

    def presentacion(self):
        print(f"hola soy {self.nombre}, mi apellido es {self.apellido} y tengo {self.edad} años.")

class Deporte:
    def __init__(self,nombre,categoria):
        self.nombre =nombre
        self.categoria =categoria

    def desempeño(self):
        print(f"me gusta el {self.nombre}")
    
    

chica1 = Chica("Agus",16,"Pelatti")
chica2 = Chica("Zoe", 16, "Blanco")

deporte1 = Deporte("Futbol", "Cuarta")

participante1 = chica1.nombre + deporte1.desempeño