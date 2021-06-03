cursos = ["Python","Django","Flask"]

niveles = ("Basico","Intermedio","Avanzado")

#crear una tupla apartir de una lista

cursos_tupla = tuple(cursos)
print(cursos_tupla)
print(type(cursos_tupla))

#crear una lista de una tupla

niveles_lista = list(niveles)
print(niveles_lista)
print(type(niveles_lista))