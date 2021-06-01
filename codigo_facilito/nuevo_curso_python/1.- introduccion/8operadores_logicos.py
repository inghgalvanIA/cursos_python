"""

operadores logicos nos permiten obtener un valor booleano
mediante la comparacion de booleanos

son:
    and
    or
    not
"""

#and (todas las partes de la comparativa deben ser verdadero para obtener verdadero)

res_and = 10 == 10 and True and "hola" == "hola"

print(res_and)

#or (por lo menos una de las comparaciones debe ser verdadera para obtener verdadero)

res_or = 10 == 30 or 5 == 10 or "hello" == "hello"
print(res_or)

#not (nos permite negar un operador booleano)

res_not = not True
print(res_not)