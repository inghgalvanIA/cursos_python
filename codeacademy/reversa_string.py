# Write your reverse_string function here:


def reverse_string(word):

    if len(word) > 0:  
        resultado = word[::-1]
    else:
        resultado = word        


    return resultado 

# Uncomment these function calls to test your  function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print