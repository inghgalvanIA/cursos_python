lenguajes = "Python Ruby Java Rust C++ C"
lenguajes_dos = "Python-Ruby-Java-Rust-C++-C"
lenguajes_tres = ["Python","Ruby","Java","Rust"]
#el metodo split nos permite generar una lista apartir de un string

listado_lenguajes = lenguajes.split()
print(listado_lenguajes)

#si queremos separarlo por otro caracter

listado_lenguajes_dos = lenguajes_dos.split("-")
print(listado_lenguajes_dos)

#se puede agregar oro lemento de solo ocupar la funcion ciertas veces
#nombre_variable = nombre_string.split(carater_dividir, numero de veces a utilizar)
listado_lenguajes_tres = lenguajes_dos.split("-",2)
print(listado_lenguajes_tres)

#el metodo join nos permite generar un string a partir de una lista
string_lenguajes = "/".join(lenguajes_tres)
print(string_lenguajes)
print(type(string_lenguajes))