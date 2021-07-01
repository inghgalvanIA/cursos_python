"""
para definir e inicializar objetos al momento de crearlo utilizaremos el metodo init

"""

class Usuario:
    # Object
    def __init__(self,username,password):
        self.username = username
        self.password = password

user1 = Usuario("user1","password1")
user2 = Usuario("user2","password2")
user3 = Usuario("user2","password")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)