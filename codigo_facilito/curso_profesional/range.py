lista = [1,2,3,4,5,6]

for valor in range(10):#crea un rango de numeros en este caso del 0  al 9
    print(valor)


for valor_uno in range (5,14):#range(valor inicial, valor final)
    print(valor_uno)

for valor_dos in range (1,20,2):#range(valor inicial, valor final, numero de saltos)
    print(valor_dos)

for valor_tres in range(len(lista)):
    print("indice",valor_tres, "valor", lista[valor_tres])

