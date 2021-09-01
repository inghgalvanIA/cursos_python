"""
1.- Se ejecuta de manera automática cuando instanciamos un nuevo objeto de una clase. 
2.- Tiene un nombre definido en el lenguaje, por ejemplo en python es init 
3.- Su tarea es inicializar el objeto ejemplo un contador en 0 .

se declara el metodo

def __init__(self):


"""

class Usuario:
  
    def __init__(self,nombre):
        #metodo constructor       
        self.nombre = nombre

    def saludar(self,saludo):
        print(saludo + self.nombre)

Hector = Usuario("Hèctor")


Hector.saludar("Hola: Mi nombre es: ")


# ejemplo de inicializar un contador

class Contador:
    def __init__(self):
        self.conteo = 0
