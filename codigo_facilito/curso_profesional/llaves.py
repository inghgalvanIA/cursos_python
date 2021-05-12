diccionario = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}

resultado = diccionario.keys()#retorna un objeto  dict key donde se ven todas las llaves
resultado_dos = tuple(resultado)#al retornar un objeto keys lo podemos pasar a lista o tupla
resultado_tres = diccionario.values()#retorna un objeto dict_values con los valores del diccionario
resultado_cuatro = diccionario.items()#retorna un objeto dict_items con tanto llaves como valores

print(resultado)
print(resultado_dos)
print(resultado_tres)
print(resultado_cuatro)