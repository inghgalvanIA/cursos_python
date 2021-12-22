# para tener un tipado estatico se va seguir la siguiente sintaxis

# nombre_variable: type = valor

a: int= 5
b: str= "Hola"
c: bool= True



print(a,b,c)

#se puded pedir que el valor ingresado sea de un tipo de valor en especifico y que una funcion regrese un valor en especifico

def suma(valor_uno: int,valor_dos: int) -> int:
    resultado = valor_uno + valor_dos
    return resultado

res_uno = suma(10,20)
res_dos = suma("10","20")
tipo_res = type(res_uno)
tipo_res_dos = type(res_dos)

print(res_uno)
print(tipo_res)
print("solo es un tema d eprueba con str desde el principio no funcionara y se tendra un comprotamiento normal")
print(res_dos)
print(tipo_res_dos)