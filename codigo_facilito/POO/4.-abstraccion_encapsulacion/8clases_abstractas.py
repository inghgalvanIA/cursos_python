"""
en python existe clases llamadas abstractas

la clase abstracta busca definir un objeto en manera generals


"""

#importa en metodo abc

from abc import ABC,abstractclassmethod, abstractmethod


#creamos una clase abstracta
class AbstractStructure(ABC):
    @abstractmethod
    def obtener():
        pass
    @abstractmethod
    def agregar():
        pass

class FilaBancos:
    usuarios ={}

    def siguiente_usuario(self,numero):
        #implemenmtacion
        return self.usuarios.obtener[numero]
    def formar_usuarios(self,usuario):
       usuarios(ticket) = usuario 

class Nash():
    datos ={}
    def obtener(self,llave):
        datos[llave]
    def agregar(self,llave,valor):
        datos(llave)= valor

class Queue:
    datos = []

    def obtener(self):
        datos[e]

    def agregar(self,llave,valor):
        datos[len(datos)-1] = valor