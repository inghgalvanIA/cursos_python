#en python no hay una forma para modificar los accesos a una propiedad
#publica no se hace nada todas son publicans
#pretegida se usa _ antes del nombre
#privada se usara __ antes dle nombre



class Usuario:
    def __init__(self,nombre):
        # Metodo constructor protegida
        self._nombre = nombre
    
    def saludar(self,saludo):
        print(saludo + self.nombre)

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

class Pagina:
    def imprimir_pie_pagina(self):
        print(self.pie_pagina)

class PaginaLegal(Pagina):
    def imprimir_pie_pagina(self):
        
        print("Derechos reservados")
        super().imprimir_pie_pagina()

html = PaginaLegal()
html.pie_pagina= "<p>Hola</p>"

html.imprimir_pie_pagina()