import time

def fibo_gen():
    max_num = int(input("Cual es el numero maximo de la cadena."))
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:

            aux = n1 + n2

            if aux <= max_num:
                n1, n2 = n2, aux
                counter += 1
                yield aux
            else:
                print("Se llego a lo maximo")
                return

if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(.05)