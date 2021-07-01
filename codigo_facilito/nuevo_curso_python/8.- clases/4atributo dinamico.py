"""
Atributos de clase
atributos que le pertenenscan a una clase obligando a usar dicha clase

Atributos de instancia
atributos que le eprtenescan a un objeto obligando a trabajar con el objeto

"""

class Usuario:
    #atribiutos de la clase 
    username = "Hector"
    email = ""

#__dict__ (Atributo para ver )
user1 = Usuario()
#1.- verifica si el atributo existe dentro del objeto
#2.- verifica si el atributo existe dentro de la clase(si existe se utilzia dicho atributo)
#3.- Lanzar un error

user1.username = "Cody"
user1.password = "1234"

print(user1.username) # de instancia

print(id(user1.username))
print(id(Usuario.username))


print(user1.__dict__)