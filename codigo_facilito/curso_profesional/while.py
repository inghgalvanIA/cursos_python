numero = 123456789

contador = 0

while numero >= 1:# podremos ejecutar un bloque de codigo n cantidad de veces hasta que una condicion deje de cumplirse

    contador +=1         #bloque de codigo a cumplirse 
    numero = numero / 10
#else: lo que se ponga dentro del else se va ejecutar cuando ya no se cumpla la condicion del while
print("la cantidad de digitos del numero es",contador)