
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self, otra_persona):
        print(f"Hola {otra_persona.nombre} me llamo {self.nombre}")



hector = Persona("Hector", 31)
erika = Persona("Ericka", 27)
david = Persona("David", 18)

hector.saludar(erika)
david.saludar(hector)