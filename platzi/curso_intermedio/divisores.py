def divisor(num):
    div_num = []
    for i in range(1,num + 1):
        if num % i == 0:
            div_num.append(i)
    return div_num



def run():
    num = int(input("Ingresa un numero"))
    print(divisor(num))
    

if __name__ == "__main__":
    run()