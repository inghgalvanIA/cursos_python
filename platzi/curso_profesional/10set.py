#crear un set

my_set = {"Hola",23.3,False,True}

#crea un set por medio de una lista o tupla

my_list = [1,2,3,4]
my_set_dos = set(my_list)

print(my_set)
print(type(my_set))
print(my_set_dos)
print(type(my_set_dos))

#añadir elementos a un set
#añadir un elemento

my_set_dos.add(5)

print(my_set_dos)

#añadir multiples elementos

my_set_dos.update([8,9,10])

print(my_set_dos)

#con discard si inento eliminar un elemento que no existe no pasa nada si lo intento con remove me mandara un error

my_set_dos.discard(1)

my_set_dos.remove(2)

print(my_set_dos)

#borra un elemento aleatotio

my_set_dos.pop()
print(my_set_dos)

#limpiar el set

my_set_dos.clear()
print(my_set_dos)