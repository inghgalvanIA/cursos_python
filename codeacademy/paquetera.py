weight = int(input("¿Cual es el peso del paquete?"))

if weight <= 2:
    price = 4.50
    print("El precio del envio es de {} dolares".format(price))
elif weight > 2 and weight <= 6:
    price = 9
    print("El precio del envio es de {} dolares".format(price))
elif weight > 6 and weight < 10:
    price = 12
    print("El precio del envio es de {} dolares".format(price))
elif weight >= 10:
    price = 14.25
    print("El precio del envio es de {} dolares".format(price))   
else:
    print("error") 