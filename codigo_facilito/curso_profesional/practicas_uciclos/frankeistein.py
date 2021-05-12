capitulo_frank = ''' A qui se ingresa el texto'''
capitulo_frank.lower()
lista_capitulo_frank = capitulo_frank.split()



palabras_repetidas = []


for i in lista_capitulo_frank:
    palabras_repetidas.append(lista_capitulo_frank.count(i))


veces_repetida = max(palabras_repetidas)
indice = palabras_repetidas.index(veces_repetida)


palabra_mayor = lista_capitulo_frank[indice]


print('Palabra mas repetida: ', palabra_mayor, '\nNumero de veces que se repite: ', veces_repetida)
