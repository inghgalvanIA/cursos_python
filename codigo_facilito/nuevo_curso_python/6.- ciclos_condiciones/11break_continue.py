"""
existen 2 palabras que pueden modufucar el comportamiento de nuestros ciclos

break rompera ede forma inmediate el ciclo

continue omitira la accion del ciclo y continuara con la siguiente iteracion

"""

titulo_curos = "Curso profesional de Python"

for caracter in titulo_curos:
    if caracter == "P":
        break
    elif caracter == "o":
        continue
    print(caracter)