"""
scope o alcance de las variables
variables globales pueden ser utilizadas en cualquier bloque
- funcion
- condicion
- ciclo

variable local solo puede ser utilizada en el bloque que fue creada

para vizualizar el objeyo unico
id(objeto)

para modificar una variable global dentro de un bloque 
podemos usar la palabra global
global nombre_variable

con esto indicaremos que dentro del bloque local utilizaremos la variable global
"""
#variable global
animal = "leon"
animal_dos = "Gorila"

def imprimir_animal():
    global animal_dos

    #variable local
    animal = "Ballena"
    animal_dos = "Codorniz"
    print(animal)
    print(id(animal))
    print(animal_dos)

imprimir_animal()
print(animal)
print(id(animal))

print(animal_dos)