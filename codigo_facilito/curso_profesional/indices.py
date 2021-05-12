cursos = ["python","django","flask","c","c++","c#","java","php"]
curso = cursos[2]#mostrar el dato del indice 2 de la lista
sub = cursos[0:3]#crear una sublista [dato inicial:dato final]
sub_dos = cursos[4:]#crea una sublista de la posicion 4 inicial hasta el termino
sub_tres = cursos[0:7:2]#crear una sublista del inicio a la posicion 7 de 2 en 2
sub_cuatro = cursos[::-1]#crear una lista en orden al revez

print(curso)
print(sub)
print(sub_dos)
print(sub_tres)
print(sub_cuatro)