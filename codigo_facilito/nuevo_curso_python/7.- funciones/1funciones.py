"""
para crear una funcion nos apoyaremos de la palabra def
el nombre de la funcion se basa en snake case


def nombre_funcion(parametros)
    codigo
    return

mandar llamar la funcion
nombre_funcion(argumentos)
"""


def suma():
    numero_uno = int(input("Ingresa el numero entero: "))
    numero_dos = int(input("Ingresa el segundo numero: "))
    resultado = numero_uno + numero_dos
    return resultado

print(suma())
