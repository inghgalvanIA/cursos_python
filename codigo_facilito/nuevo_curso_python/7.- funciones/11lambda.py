"""
una funcion lambda 
es una funcion anonima y esta es expresada en una sola linea
por lo regular estas funciones son muy pequeñas

lambda parametros : operacion
siemrpe retornara la linea de codigo sin el return

"""

funcion_grados = lambda grados : grados * 1.8 +32
#lambda <parametors> : <cuerpo de la funcion>

print(funcion_grados(10))

"""
otros ejemplos de lambdas

sin_parametros = lambda:True
parametros_default = lambda p1=10, p2=20 p3=30: p1+ p2 + p3

asterisco = lambda *args, **kwargs: len(args) + len(kwargs)
"""
