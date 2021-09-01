class Usuario:
    __edad = 0
    def __init__(self,nombre):
        # Metodo constructor protegida
        self._nombre = nombre
    
    def saludar(self,saludo):
        print(saludo + self.nombre)

    @property
    def edad(self):
        return self.__edad
#clase hijo heredando de Usuario
class Empleado(Usuario):

    salario = 0

    def modificar_salario(self,salario):
        self.__salario = salario

    def ver_salario(self):
        print(self.__salario)
    
    def saludar(self):
        super().saludar("Hola")
        print(f"Mi nombre es: {self._nombre} y gano {self.__salario}")

empleado = Empleado("Hector")
empleado.saludar()
empleado.modificar_salario(1000)
empleado.ver_salario()
empleado.saludar()
empleado.edad = 20
print(empleado.edad)

