lista = [8.17,90,1,50,44,1.32,8.17]

lista.sort()
#lista.sort(reverse=True) en esta se pone de manera descendente
menor = lista [0]#selecionar el dato dependiendo de la posicion 
menor_uno = min(lista)#para selecionar el numero mas chico
mayor = max(lista)#para selecionaer el numero mas alto
longitud = len(lista)#para checar el numero de la lista
resultado = 8 in lista #buscar un valor dentro de la lista
indice = lista.index(8.17)#va a decir el indice donde esta
contador = lista.count(8.17)#contar el numero de veces que se repite el numero


print(lista)
print(menor)
print(menor_uno)
print(mayor)
print(longitud)
print(resultado)
print(indice)
print(contador)