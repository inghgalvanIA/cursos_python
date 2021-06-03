numeros = (1,2,3,4)
#uno, dos , tres, cuatro = 1,2,3,4
uno, dos , tres, cuatro = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)

#para guardar los ultimos valores en una sola variable *

numeros_dos = [1,2,3,4,5,6]
unon, dosn, tresn, cuatron, *restos_valores = numeros_dos
print("###################################")
print(unon)
print(dosn)
print(tresn)
print(cuatron)
print(restos_valores)

#si se quisieran omitir los calores restantes se usar *_
#unon, dosn, tresn, cuatron, *_ = numeros_dos

#omitir valores medios
numeros_tres = [1,2,3,4,5,6,7,8,9,10]

unot, dost, trest, cuatrot, *_ ,nuevet ,diezt = numeros_tres
print("###################################")
print(unot)
print(dost)
print(trest)
print(cuatrot)
print(nuevet)
print(diezt)