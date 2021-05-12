diccionario = {"a": 1, "b": 2, "c":3, "a": 4 }

resultado = diccionario["a"]#imprimir solo la llave a del diccionario
resulrado_uno = "z" in diccionario#conocer con un booleano si la llave z existe
resultado_dos = diccionario.get("a","aparece si no existe la llave")#si existe una llave a nos regresara su valor
resultado_tres = diccionario.setdefault("z","si no exite se agrega esta llave")#si la llave no se crea se crea una

print(resultado)
print(resulrado_uno)
print(resultado_dos)
print(resultado_cuatro)