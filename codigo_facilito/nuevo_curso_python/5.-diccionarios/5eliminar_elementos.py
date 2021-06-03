diccionario = {"a":1,"b":2,"c":3,"d":4}
print(diccionario)
#eliminar un elemento
# del nombre_diccionario[llave]
del diccionario["a"]
print(diccionario)

#extraer y eliminar un valor .pop(llave)
valor =diccionario.pop("b")
print(valor)
print(diccionario)

#eliminar todos los elementos del diccionario (reiniciarla)
diccionario.clear()
print(diccionario)