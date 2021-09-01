#los metodos son funciones que le pertenecen el objetos
#alaterar o modificar una propiedad
#retornar el valor de una propiedad
#hacer calculos con los valores de las propiedades

# def nombre_metodo(self):
#lineas de codigo metodo

#y la instacia del mentodo
#nombre_objeto.nombre_instancias()

class Usuario:
    nombre = "Hector"
    #self hace referencia la mismo objeto
    def saludar(self):
        print(f"Mi nombre es {self.nombre}")


Hector = Usuario()
Hector.nombre = "Hector"

Hector.saludar()

