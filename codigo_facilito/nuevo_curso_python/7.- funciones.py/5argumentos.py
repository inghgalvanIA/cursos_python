"""
seremos capaces de crear funciones con una n cantidad de argumentos
sum() suma total de todos los elementos de la estructura
"""
lista = [10,10,5,7,10]
print(lista)
suma_lista = None

def promedio(listado):
    suma_lista = 0
    num_elementos = len(listado)
    for i in listado:
        suma_lista = suma_lista + i
    respuesta = (suma_lista/num_elementos)
    print(respuesta)
    return respuesta


resultado = promedio(lista)
print(resultado)