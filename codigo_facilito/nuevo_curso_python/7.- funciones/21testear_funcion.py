# Docstring (comentario en la primera linea del script)
# __doc__ modulo paa ver comentarios solo lo tienen (Modulos, clases, metodos y funciones)

def suma(numero_1,numero_2):

    """
    la funcion suma dos numeros enteros

    Argumentos:

    numero_1 (int)
    numero_2 (int) 

    se retrna la suma d elos parametros

>>> suma(10,20)
30

>>> suma(20,20)
40

    """
    return numero_1 + numero_2

resultado = suma(10,20)
print(resultado)

#para ver comentatios del archivo __doc__
print(suma.__doc__)