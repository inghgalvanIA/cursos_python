"""
enumerate la ocuparemos de apoyo para ennumerar una lista o tupla
por default es 0 pero si se desea empezar de otro indice se anexa como segundo argumento


"""

numeros = [10,20,30,40,50]

for indice, numero in enumerate(numeros):
    print(indice, numero)