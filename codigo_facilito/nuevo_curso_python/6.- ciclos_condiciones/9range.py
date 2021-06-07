"""

range() esta funcion crearemos una secuencia de numero que podremos iterar
range por defecto en 0 y el numero que usemos en la funcion no sera tomado en cuenta
range(numero_final + 1)

"""

rango = range(11) # 0 -10

print(rango)
print(type(rango))

for valor in rango:
    print(valor)

#agregadno otro inicio que no es cero
#range(inicio,final,saltos)

for valor_dos in range(5,100,5):
    print(valor_dos)