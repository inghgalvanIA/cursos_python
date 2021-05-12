estudiantes = {
    "México":10,
    "Colombia":15,
    "Panama":4,
}

#iterar directamente en el diccionario
for pais_uno in estudiantes:

    print(pais_uno)

#iterar  en las keys del diccionario
print("**************************************************")

for pais_dos in estudiantes.keys():

    print(pais_dos)

#iterar en las values del diccionario
print("**************************************************")

for numero_estudiantes in estudiantes.values():

    print(numero_estudiantes)

print("**************************************************")  


#iterar en los items 
for pais_uno,numero_estudiantes in estudiantes.items():

    print(pais_uno,numero_estudiantes)

print("**************************************************")