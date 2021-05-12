class Usuario:
    def __init__(self,username="",correo="",nombre=""):
        self.username = username
        self.correo = correo 
        self.nombre = nombre
    def saludo(self):
        return "Hola soy un usuario" + self.nombre
    def mostrar_username(self):
        print(self.username)
    def mostrar_nombre(self):
        print(self.nombre)

codi = Usuario("Codi","codigo@codigo.com","Codigo")

resultado = codi.saludo()

print(codi)