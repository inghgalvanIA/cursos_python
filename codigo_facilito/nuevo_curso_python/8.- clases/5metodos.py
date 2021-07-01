"""
debemos estandarizar la creacion de metodos para crear objetos 
tener los mismos atributos

crear una funcion dentro de nmuestra clase

def nombre_funcion(self) *self hace referencia al objeto mismo
"""

class Usuario:
    #creacion del metodo
    def inicializar(self, username, password):
        #añadiendo atributos al objeto
        self.username = username
        self.password = password

#creacion de los objetos
user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

#llamar la funcion inicializar

user1.inicializar("user1","password1")
user2.inicializar("user2","password2")
user3.inicializar("Hector","estrambotico")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)