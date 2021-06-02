#indices            0       1       2        3       4        5
lista_cursos = ["Python","Django","Flask", "Ruby", "Java", "Rust"]

#añadir nuevos elementos a la lista 
#nombre_lista.append(dato a agregar)

lista_cursos.append("MongoDB")

print(lista_cursos)

#conocer la longgitud de la lista
#len(nombre_lista)

print(len(lista_cursos))

#agregar un elemento por medio de un indice en especifico
# nombre_lista.insert(indice,dato a insertar)
lista_cursos.insert(1,"C#")
print(lista_cursos)

#se puded hacer una lista de otras listas
#nombre_lista_uno.extend(nombre_lista_dos)
lista_curso_dos =["c","c++","Docker","Pygame"]
lista_cursos.extend(lista_curso_dos)
print(lista_cursos)

#eliminar un elemento de la lista 
#nombre_lista.remove(Dato a eliminar)
lista_cursos.remove("MongoDB")
print(lista_cursos)

#otra forma de eliminar con indice
del lista_cursos[1]
print(lista_cursos)

#eliminar todos los datos de la lista (reiniciarla)
lista_cursos.clear()
lista_cursos.append("Python")
print(lista_cursos)
