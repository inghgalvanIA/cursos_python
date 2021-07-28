"""
las propiedades de la clase hijo no ñas tendra el clase padre


"""


#clase padre 
class Usuario:
    def __init__(self,nombre):
        # Metodo constructor
        self.nombre = nombre
    
    def saludar(self,saludo):
        print(saludo + self.nombre)

#clase hijo heredando de Usuario
class Empleado(Usuario):

    salario = 0

    def modificar_salario(self,salario):
        self.salario = salario

    def ver_salario(self):
        print(self.salario)
    
    def saludar(self):
        print(f"Mi nombre es: {self.nombre} y gano {self.salario}")

empleado = Empleado("Hector")
empleado.saludar()
empleado.modificar_salario(1000)
empleado.ver_salario()
empleado.saludar()