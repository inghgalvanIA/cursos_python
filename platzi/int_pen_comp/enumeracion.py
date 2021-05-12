objetivo = int(input("Escoje un entero: "))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1

if  respuesta**2 == objetivo:
    print(f"la raiz cuadrada de {objetivo} es {respuesta}")

else:
    print(f"el numero {objetivo} no tienen una raiz cuadrada exacta")