def divisor(num):
    div_num = []
    for i in range(1,num + 1):
        if num % i == 0:
            div_num.append(i)
    return div_num



def run():
    num = (input("Ingresa un numero"))
    assert num.isnumeric(),"ingrese un numero"
    assert num < 0, "ingrese un numero positivo"
    num_int = int(num)
    print(divisor(num_int)
    

if __name__ == "__main__":
    run()