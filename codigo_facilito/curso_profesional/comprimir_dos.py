tupla = (1,2,3,4,5,6)# se crea una tupla

lista = [10,20,30,40]# se crea una lista

tupla_dos = (100,200,300,400)


resultado = zip(tupla, lista, tupla_dos)
resultado = tuple(resultado)

print(resultado)


