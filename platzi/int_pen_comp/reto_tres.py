print("¿Cual es el nombre del usuario 1?")
usuario_uno = input()
print("¿cual es la edad del usuario 1?")
edad_uno = int(input())
print("¿cual es el nombre del usuario 2?")
usuario_dos = input()
print("¿cual es la edad del usuario 2?")
edad_dos = int(input())

if edad_uno > edad_dos:
    print(f"{usuario_uno} es mayor que {usuario_dos}")

elif edad_uno < edad_dos:
    print(f"{usuario_dos} es mayor que {usuario_uno}")

else:
    print("ambos usuarios tienen la misma edad")    