#clase padre 
"""

Extender un metodo de la clase padre para editarlo

"""


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
        super().saludar("Hola")
        print(f"Mi nombre es: {self.nombre} y gano {self.salario}")

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