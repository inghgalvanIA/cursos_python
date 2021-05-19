""" 
Crear, con un list comprehension, una lista de todos los multiplos de 4 que a la vez tambièn son mùltiplos de 6 y de 9,
hasta 5 digitos


"""


lista = [i for i in range(1,10000)if i % 4 == 0 and i % 6 ==0 and i % 9 ==0]

print(lista)