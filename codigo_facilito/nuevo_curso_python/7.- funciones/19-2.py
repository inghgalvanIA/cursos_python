def pares():
    for numero in range(0 , 12, 2):
        yield numero


generador = pares()

while True:
    try:
        par = next(generador)
        print(par)

    except StopIteration:
        print("El generador finalizo")
        break
    
