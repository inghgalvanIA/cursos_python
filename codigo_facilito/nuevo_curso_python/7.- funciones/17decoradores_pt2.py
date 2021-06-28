def funcion_a(funcion_b):

    def funcion_c(*args,**kwargs):
        print(">>>> Antes del llamado")

        resultado = funcion_b(*args,**kwargs)

        print(">>> Despues del llamado")

        return resultado

    return funcion_c

@funcion_a
def suma(numero_uno,numero_dos):
    return numero_uno + numero_dos

resultado = suma(10,20)
print(resultado)