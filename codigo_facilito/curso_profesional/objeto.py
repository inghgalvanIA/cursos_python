"""
todas las clases que creemos van a estar heredando de una clase en comun
hay 2 formas de crear las clases
"""
#forma 1
class Gato:
    def __init__(self,nombre):
        self.nombre =nombre

    def __str__(Self):
        return Self.nombre
#forma 20
class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(Self):
        return Self.nombre

gato = Gato("Bigotes")
gato.edad = 6
pato = Pato("Lucas")

print(gato.__dict__)
print(pato.__dict__)

print(gato)
print(pato)