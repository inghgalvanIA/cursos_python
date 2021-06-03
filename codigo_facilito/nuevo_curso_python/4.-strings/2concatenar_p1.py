"""

Un string es inmutable (no podemos cambiarlo en tiempod e ejecucion)
pero si podemos generar nuevos string a partir de otros

"""

nombre = "Héctor Rosendo"
apellido = "Galvàn"

nombre_completo = "Sr. " + nombre + " " + apellido + "."
nombre_completo_dos = "Sr. %s %s. " %(nombre, apellido)
nombre_completo_tres = "Sr. {} {}.".format(nombre,apellido)
nombre_completo_cuatro = f"Sr. {nombre} {apellido}."


print(nombre_completo)
print(nombre_completo_dos)
print(nombre_completo_tres)
print(nombre_completo_cuatro)