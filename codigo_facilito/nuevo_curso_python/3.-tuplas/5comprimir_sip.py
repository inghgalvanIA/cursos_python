"""
comprimir inverso para generar tuplas

"""



lista = [1,2,3,4,5]

tupla = (10,20,30,40,50)

lista_dos = (100,200,300,400,500)

tupla_dos = (1000,2000,3000,4000,5000)

resultado = zip(lista, tupla,tupla_dos,lista_dos)# -> objeto zip
resultado = tuple(resultado)
print(resultado)