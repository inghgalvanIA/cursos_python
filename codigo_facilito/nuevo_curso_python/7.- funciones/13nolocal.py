"""

variables locales solo pueden ser creadas 
el el bloque fueron creadas

con nonlocal le decimos al programa que no es que queremos crear una variable
local si no que queremo modificar la variable de un scope superior



"""


e = "e" #variables globales

def funcion_principal():
    a = "a" # variables locales
    b = "b"

    print(b)
    def funcion_anidada():
        c  = "c"
        nonlocal b
        b = "cambio de valor"

        print(a)
        print(b)

        print(e)

    funcion_anidada()
    #print(c)
funcion_principal()