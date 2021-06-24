"""

closure es una funcion que puede generar de forma dianmica
a otra funcion, y esta funcion creada puede acceder a las variables locales 
aun cuando la primera haya finalizado


"""

def saludar(username):
    mensaje = f"Hola {username}" # variable local

    def mostrar_mensaje():
        print(mensaje)

    return mostrar_mensaje

username = "Cody"
respuesta = saludar(username)

username = "Eduardo"

respuesta()
respuesta()
respuesta()
