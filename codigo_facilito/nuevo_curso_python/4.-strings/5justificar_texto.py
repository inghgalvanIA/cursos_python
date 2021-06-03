mensaje = "hola mundo"

#Hay 3 formas de justificar texto
#ljust -> justificar a la izquierda .ljust(numero de espacios)

mensaje_izq = mensaje.ljust(20)
print(mensaje_izq,".")

#rjust -> justificar a la derecha .rjust(numero de espacios)
mensaje_der = mensaje.rjust(20)
print(mensaje_der)


#center -> centrar
mensaje_center = mensaje.center(20)
print(mensaje_center)