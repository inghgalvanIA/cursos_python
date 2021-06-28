"""
labmdas o ciudadanos de priemra clase

funciones pueden ser asignadas a variables
pueden ser utilziadas como argumentos


"""

def centigrados_a_farehenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centigrados_a_farehenheit

print(type(mi_funcion))

print(mi_funcion(12))