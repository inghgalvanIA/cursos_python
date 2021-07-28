#los metodos son funciones que le pertenecen el objetos
#alaterar o modificar una propiedad
#retornar el valor de una propiedad
#hacer calculos con los valores de las propiedades


class Usuario:
    nombre = "Hector"
    #self hace referencia la mismo objeto
    def saludar(self):
        print(f"Mi nombre es {self.nombre}")


Hector = Usuario()
Hector.nombre = "Hector"

Hector.saludar()

