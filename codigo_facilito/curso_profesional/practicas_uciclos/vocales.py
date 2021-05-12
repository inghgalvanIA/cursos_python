print("ingresa un mensaje")
mensaje = input()
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0


for caracter in mensaje:
    if caracter == "a":
     contador_a += 1
    if caracter == "e":
     contador_e += 1
    if caracter == "i":
     contador_i += 1
    if caracter == "o":
     contador_o += 1
    if caracter == "u":
     contador_u += 1

num_vocales = contador_a + contador_e + contador_i + contador_o + contador_u

print("el numero de a", contador_a)
print("el numero de e", contador_e)
print("el numero de i", contador_i)
print("el numero de o", contador_o)
print("el numero de u", contador_u)
print("el total de vocales es ",num_vocales)



