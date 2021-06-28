"""
si agregamos valores directamente como argumentos

si deseamos que un parametro pueda recibir una n cantidad de arugumentos
def nombre_funcion(*parametro)

por convencion todo los parametros con multiple argumentos 

se deben de llamar *args

"""



def promedio(*args):
    print(args)
    print(type(args))
    return sum(args) / len(args)

def combinacion(p1,p2,*args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

# resultado = promedio(10,10,5,7,10)
# print(resultado)

combinacion(10,20,3,4,5,6,7)

