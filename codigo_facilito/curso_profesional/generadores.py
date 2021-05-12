def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1,maximo+1):
        yield numero * posicion, numero, posicion
#yield retorna el resultado sin terminar la funcion


for resultado,numero, posicion in tabla_multiplicar(9):
    print(str(numero) + " * " + str(posicion) + " = " + str(resultado) ) 