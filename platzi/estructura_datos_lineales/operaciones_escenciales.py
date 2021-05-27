fruits = ["Manzana","Banana","Fresa","Cereza"]

#agregar valores a la lista
fruits.append("Kiwi")
print(fruits)

#agregar lista ordenanda
print("lista ordenada con sort")
fruits.sort()
print(fruits)

#obtener el ultimo elemento
print("obteniendo el ultimo elemento")
ultimo_elemento = fruits.pop()
print(ultimo_elemento)

#Sustituyendo un valor
print("sustituynedo la primera posicion")
fruits.insert(0,"Mandarina")
print(fruits)

#remover un valor
print("remover el valor Kiwi")
fruits.remove("Kiwi")
print(fruits)