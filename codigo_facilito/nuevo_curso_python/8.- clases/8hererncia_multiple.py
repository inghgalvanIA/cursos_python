"""
python permite la herencia multiple

las clases padre pueden heredar de otras clases padre

"""
class Animal():
    
    def tipo(self):
        print("Es una numal")


class Mascota(Animal): #Clase Padre

    def comer(self):
        print("La mascota come.")

    def dormir(self):
        print("La mascota duerme")


class Felino: #clase padre 2

    def cazar(self):
        print("El felinno casa")


class Gato(Mascota,Felino): # Clase Hija
    pass

patricio = Gato()

patricio.comer()
patricio.dormir()
patricio.cazar()
patricio.tipo()



