def crear_mensaje(nombre):#variables dentro de la funciones tendra el nombre de parametro
    mensaje = "Hola {}, bienvenido al curso de Python de codigo facilito".format(nombre)

    return mensaje

nuevo_mensaje = crear_mensaje("Hector")#variable que pongamos al momento de llamar una funcion se llaman argumento
print(nuevo_mensaje)