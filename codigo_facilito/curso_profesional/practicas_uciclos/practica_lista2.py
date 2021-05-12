n = 10
lista = []

print("ingrese los valores que desea promediar maximo 10")
for valor in range (1,11):
    print("ingresa el valor: ",valor, ":")
    item = int(input())
    lista.append(item)
print("la lista de numeros es",lista)

suma = lista[1] + lista[2] + lista[3] + lista[4] + lista[5]+ lista[6] + lista[7] + lista[8] + lista[9] + lista[10]
promedio = suma / 10
mayor = max(lista)
menor = min(lista)


print("la lista es", lista)
print("el suma total es", suma)
print("el promedio es", promedio)
print("el numero mayor es", mayor)
print("el numero menor es", menor)
