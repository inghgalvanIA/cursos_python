"""
generador es un tipo de funcion la cual retorna objetos la cual podemos
iterar 

yield suspenderemos de manera temporal la ejecucion de la funcion
despues de retornar se regresara 
"""

def pares():
    for numero in range(0,100,2):
        yield numero

        

for par in pares():
    print(par)