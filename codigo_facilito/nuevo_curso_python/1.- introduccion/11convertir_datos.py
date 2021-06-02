"""
podemos convertir datos con ayuda d ela funciones

int() convertir a entero
str() convertir en string
float() convertir en flotante

legantemente no se convierte si no se crea un string,float a partir de un entero

"""

edad = int(input("¿Cual es tu edad?"))
altura = float(input("¿Cual es tu altura?"))
autorizacion =  input("¿Autorizas el programa? (si/no)")

print(edad)
print(type(edad))

print(altura)
print(type(altura))

autorizacion = autorizacion == "si"
print(autorizacion)
print(type(autorizacion))
