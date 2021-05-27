#Lista
"""opósito general, de índices con tamaños dinámicos. Ordenables lista =[].
Usaria las listas para almacenar una serie de números, una lista de palabras,y básicamente cualquier cosa. """
print("Lista")
Lista_uno = ["Manzana", "Banana", "Cereza", "Kiwi"]
print(Lista_uno)

#Tupla
"""Tuplas: Inmutables, no se pueden añadir más elementos. Utiles para constantes por ejemplo coordenadas, direcciones. Es de tipo secuencial. tupla =()
Las usuaría cuando sé exactamente el tamaño que tendrán mis datos. """
print("Tupla")
Tupla_uno = ("Carro","Autobus","Avion")
print(Tupla_uno)

#Conjunto
"""Conjuntos: Almacenan objetos no duplicados.(Teoría de conjuntos), son de acceso rápido, aceptan operaciones lógicas, son desordenados.set() conjunto={1,2,3,4}
Usaría un casteo entre conjuntos y listas cuando quiero eliminar duplicados de una lista. """
print("Conjunto")
#primera forma conjunto {valorx,valorx1,valor2}
conjunto_uno = {"Chivas","Pumas","Morelia","America"}
print(conjunto_uno)
#segunda forma conjunto set()
lista_conjunto = ["Dallas","Browns","Rams","Lions"]
conjunto_dos = set(lista_conjunto)
print(conjunto_dos)


#Diccionario
""" Diccionarios: Pares de llaver valor, arrays asociativos (hash maps), son desordenados, y muy rápidos para hacer consultas. diccionario ={'Llave':"Valor"}
Los usaría para almacenar datos, listas, objetos que perfectamente pueden volverse un dataframe, o un defaultdict"""
print("Diccionario")
#Formoa uno diccionario dic = {llave:valor,llave1:valor1}
dic_uno = {"Director":"Jaime Valdez","Subdrector":"Raul Gutierrez","Secretario":"Jaime Valdez"}
print(dic_uno)
#Forma dos diccionario dict(llave=valor,llave1=valor1)
dic_dos = dict(lakers=["Lebron james","Anthony Davis"],clippers=["Patrick Beverley","Amir Coffey"])
print(dic_dos)