"""
Ciclos while

ejecutar un ciclo n cantidad de veces hasta que una condicion deje de cumplirse

utilziaremos si no sabemos el numero de condiciones que vamos a realizar

while condicion:
    codigo
else: si al condicion no se cumple
    codigo
"""

contador = 1

while contador <= 10:
    print(contador)

    contador = contador + 1

print("###########################")

numero = 123456789
contador_digitos = 0

while numero >= 1:
    #contador_digitos = contador_digitos + 1
    contador_digitos += 1
    
    numero = numero / 10

else:
    print("Fin del ciclo while")
print(contador_digitos)