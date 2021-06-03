titulo_curso = "Curso profesional de Python, donde aprenderemos Python"

# para buscar un cadena dentro de una cadena

#para contar el numero de veces que se repite una cadena dentro de otra cadena

num_considencias = titulo_curso.count("Python")
print(num_considencias)

#para ver si un string existe dentro de un string

print("Curso" in titulo_curso)

print("curso"  in titulo_curso.lower())

#para saber si un string empeiza con otra string

print(titulo_curso.startswith("Cursos"))

#para saber su un string finaliza con otro string

print(titulo_curso.endswith("Python"))