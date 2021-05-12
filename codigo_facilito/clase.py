#se crea una clase con class debe de empezar con mayusculas
class Usuario:
   def saluda (self,nombre):
      return "Hola soy un usuario" + nombre

codi = Usuario()
facilito = Usuario()

print(codi.saluda("Codi"))
print(facilito.saluda("Facilito"))