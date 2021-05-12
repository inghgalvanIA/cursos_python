nombre = input("¿Cual es tu nombre?\n")

edad = int(input("¿cual es tu edad?\n"))

peso = float(input("¿cual es tu peso?\n"))

autorizado = input("¿Estas autorizado?(si/no)\n") == "si"

print("Hola ", nombre)
print("tu edad es ", edad , "años")
print("tu peso es ", peso , "Kg")
print("tu respuestas de autorizacion es " ,autorizado)