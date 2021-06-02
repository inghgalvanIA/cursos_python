"""

ES una estructura de datos en la cual manejamos otros datos
hay 2 formas de crear una lista:

 nombre_lista = list(datos en la lista)

 nombre_lista = [datos de la lista]

 cada elemnto tiene un indice y empieza con 0

de preferencia crear listas de un solo tipo de dato para evitar errores
"""
#     = [   0    ,1, 2  ,  3 ]
lista = ["texto",10,12.6,True]

print(lista)

#indices            0       1       2        3       4
lista_cursos = ["Python","Django","Flask", "Ruby", "Java"]
print(lista_cursos)
#obtener un elemento del listado [numero_inidice]
primer_curso = lista_cursos[0]
print(f"el primer curso es {primer_curso}")

segundo_curso = lista_cursos[1]
print(f"el segundo curso es {segundo_curso}")


#se puede trabajar los indice con numero negativo
#indices            -5       -4      -3       -2       -1
#lista_cursos = ["Python","Django","Flask", "Ruby", "Java"]


ultimo_curso = lista_cursos[-1]
print(f"el ultimo curso es {ultimo_curso}")

penultimo_curso = lista_cursos[-2]
print(f"el penultimo curso es {penultimo_curso}")