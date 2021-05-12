def suma(*args):#para recibir n numero de argumentos
    total = 0#iniciamos un contador en 0
    print(args)#si imprimimos nos damos cuenta que es una tupla
    for valor in args:#va recorrer la iteracion en args
        total+=valor#total ira sumando las posicion de vlor
    return total#regresa el valor total
resultado = suma(10,20,30,40,50)
print(resultado)
