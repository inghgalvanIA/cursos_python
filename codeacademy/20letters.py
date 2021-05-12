# Write your add_exclamation function here:

def add_exclamation(word):
    tamaño_palabra = len(word)
    print(tamaño_palabra)
    resultado = word

    while tamaño_palabra < 20:
        resultado = resultado + "!"
        tamaño_palabra += 1
    
    return resultado

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn