num_uno = int(input("escoge el primer valor: "))

num_dos = int(input("escoge el segundo valor: "))

if num_uno > num_dos:
    print(f"el valor {num_uno} es mayor que {num_dos}")
elif num_uno < num_dos:
    print(f"el valor {num_dos} es mayor que {num_uno}")

else:
 
    print("ambos valores son inguales")