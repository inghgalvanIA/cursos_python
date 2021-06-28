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

Usuario.username = "Usuario_uno"
Usuario.email = "info@cf.com"
#imprimir atributo
print(Usuario.username)
print(Usuario.email)