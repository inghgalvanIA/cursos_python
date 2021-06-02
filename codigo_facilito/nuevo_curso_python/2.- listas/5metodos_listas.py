lista = [8, 9,0 ,1, 5, 44, 132, 600, 3, 4 ]

#ordenar listas en orden 

lista.sort()
print(lista)

#ordenar la lista en reversa
lista.sort(reverse=True)
print(lista)

#conocer el numero mayor

num_mayor = max(lista)
print(f"El numeor mayor de la lista es {num_mayor}")

#conocer el numero menor
num_menor = min(lista)
print(f"El numero menor de la lista es {num_menor}")

#conocer si un numero se encuentare en nuestra lista

print(8 in lista)

#conocer su un numero NO se encuentra en la lista
print(123 not in lista)

#para saber el indice de un dato que conoscamos

index = lista.index(8)
print(index)