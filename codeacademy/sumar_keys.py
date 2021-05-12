# Write your sum_even_keys function here:
def sum_even_keys(dict_one):
    resultado = 0
    for key in dict_one.keys():
        resultado += key
    return resultado


# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
#print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6