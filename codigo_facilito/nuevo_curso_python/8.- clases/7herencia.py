"""
podemos heredar de otra clase

"""



class Mascota:  #clase padre
    
    def comer(self):
        print("la mascota come.")
    
    def dormir(self):
        print("La mascota duerme.")

class Perro(Mascota):   #Calse hija
    pass

class Gato(Mascota):
    pass


duke = Perro()

duke.comer()
duke.dormir()

frufru = Gato()

frufru.comer()
frufru.dormir()