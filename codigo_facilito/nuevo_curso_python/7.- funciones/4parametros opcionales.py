"""

los parametros podrian ser opcionales
se asignana valores de default a los parametros

la variables por default solo pueden ir a la derecha de los argumantos

def nombre_funcion(argumento, argumento=default)

"""

def area_circulo(radio,pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(10)
print(resultado)