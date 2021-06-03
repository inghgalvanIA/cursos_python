diccionario = {"a":1,"b":2,"c":3,"d":4}

valor = diccionario["d"]
print(valor)

#conocer si una llave existe en el diccionario

valor = "z" in diccionario
print(valor)

#obtener el valor de una llave con get en caso de no existir retornoa un None
#nombre_diccionario.get(llave_a_buscar,mensaje en caso de error)

valor = diccionario.get("a", "La llave no existe en el diccionario")
print(valor)

#obtener el valor de una llave #setdefault

valor_l = diccionario.setdefault("a","la llave no existe")
print(valor_l)