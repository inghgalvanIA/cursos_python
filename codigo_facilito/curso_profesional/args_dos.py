def suma(parametro_requerido,*args):#para recibir n numero de argumentos
    total = 0#iniciamos un contador en 0
    print(args)#si imprimimos nos damos cuenta que es una tupla
    print(parametro_requerido)
    for valor in args:#va recorrer la iteracion en args
        total+=valor#total ira sumando las posicion de vlor
    return total#regresa el valor total

def usuarios_autenticados(**kwargs):
    print(kwargs)


resultado = suma("Este es un parametro requerido",10,20,30,40,50)
print(resultado)

usuarios_autenticados(codi=True,facilito=False)
