"""
conseguir los elementos conforme a demanda con generadores

"""


def pares():
    for numero in range(0,100,2):
        yield numero

    

generador = pares()

print(next(generador))
print(next(generador))
print(next(generador))