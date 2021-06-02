#indices            0       1       2        3       4        5
lista_cursos = ["Python","Django","Flask", "Ruby", "Java", "Rust"]

#podemos generar sublista a partir de una lista 

#nombre_sublista = nombre_lista[inidice_inicial:indice_final]
sublista         = lista_cursos[0:3]
print(sublista)

sublista_dos = lista_cursos[1:4]
print(sublista_dos)

#para obtener los ultimos datos d ela lista desde un indice
sublista_tres = lista_cursos[2:]
print(sublista_tres)

#para obtener los primeros incisos de la liista hasta un indice indicadop
sublista_cuatro = lista_cursos[:4]
print(sublista_cuatro)

#una sublista con saltos
#nombre_sublista = nombre_lista[inidice_inicial:indice_final:numero_saltos]
sublista_cinco = lista_cursos[1:5:2]
print(sublista_cinco)

#toda la lista con saltos de 2 en 2
sublista_seis = lista_cursos[::2]
print(sublista_seis)

#la lista inversa
sublista_siete = lista_cursos[::-1]
print(sublista_siete)