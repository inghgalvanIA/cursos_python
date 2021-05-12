class Animal:
    def comer(self):
     print("Comiendo")
    def dormir(self):
        print("Durmiendo")

class Perro(Animal):
    def __init__(self,nombre):
        self.nombre = nombre
    
    def ladrar(self):
        print("ladrando")

firulais = Perro("Firulais")
firulais.comer()
firulais.dormir()
firulais.ladrar()