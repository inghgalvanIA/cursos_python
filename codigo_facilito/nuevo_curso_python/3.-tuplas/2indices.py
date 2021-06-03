#indice       0       1        2        3       4
cursos = ("Python","Flask","Django","Rails","MondoDB")

#Escoger un indice el primero

primer_curso = cursos[0]
print(primer_curso)

#EScoger el ultimo indice

ultimo_curso = cursos[-1]
print(ultimo_curso)

#Crear una subtupla a partir de nuestra tupla

sub_tupla = cursos[1:3]
print(sub_tupla)
print(type(sub_tupla))

#los primeros de una tupla
primeros = cursos[:3]
print(primeros)