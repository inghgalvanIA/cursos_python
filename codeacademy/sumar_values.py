# Write your sum_values function here:
def sum_values(dict_one):
    resultado = 0
    for value in dict_one.values():
        resultado += value
    return resultado

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
#print(sum_values({10:1, 100:2, 1000:3}))
# should print 6