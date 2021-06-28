def suma(n1, n2):
    resultado = n1 + n2
    """ return puede returnar varios valores en una tupla """
    return resultado, "la funcion 2 retornar"

num_uno = int(input("Ingresa el primer numero: "))
num_dos = int(input("Ingresa el segundo numero: "))

resultado = suma(num_uno,num_dos)
print(f"El resultdao es: {resultado}")

print("#############multiple returns###############")

""" Si se retorna multiples valores se recomienda crear multiples variables para 
desempaquetar los valores en variables diferentes """
resultado_solo, mensaje = suma(num_uno,num_dos)
print(f"El resultdao es: {resultado_solo}")
print(mensaje)

#recomendacion un maximo de 3 valores