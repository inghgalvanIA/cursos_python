# Write your x_length_words function here:

def x_length_words(oracion,letra):
    resultado = False
    palabras = oracion.split()
    print(palabras)

    for index in palabras:
        if len(index) == letra:
            resultado = True
        else:
            continue

    return resultado

# Uncomment these function calls to test your tip function:
#print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True