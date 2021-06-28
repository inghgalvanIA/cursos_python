"""
es una funcion que toma como input una funcion
y saca un output otra funcion 

con un decorador podemos ejecutar codigo antes o despues de loa funcion a decorar

a -> funcion principal (Decorador)
b -> funcion a decorar
c -> funcion decorada

a(b):

return c

ænombre_del_decorador
def funcion_decorar():
"""
#decorador(funcion a decorar)
def funcion_a(funcion_b):
    
    def funcion_c():
        print("Antes del llamado")
        funcion_b()
        print("Despues del llamado")
    
        

    return funcion_c

@funcion_a
def saludar():
    print("Hola nos econtramos en una funcion")

saludar()

