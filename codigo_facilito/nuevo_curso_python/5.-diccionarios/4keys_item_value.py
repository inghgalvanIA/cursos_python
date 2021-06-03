diccionario = {"a":1,"b":2,"c":3,"d":4}

# keys
# values
# items

#obtener las llaves del diccionario en un objeto key
print("#################llaves###########")
llaves = diccionario.keys()
print(llaves)
print(type(llaves))
llaves = tuple(llaves)
print(llaves)
print(type(llaves))

#obtener los valores del diccionario en un objeto dict_values
print("#################valores###########")
valores = diccionario.values()
print(valores)
print(type(valores))
valores = tuple(valores)
print(valores)
print(type(valores))

#obtener todos los elementos en un objeto dict_items
print("#################elementos###########")
elementos = diccionario.items()
print(elementos)
print(type(elementos))
elementos = tuple(elementos)
print(elementos)
print(type(elementos))
