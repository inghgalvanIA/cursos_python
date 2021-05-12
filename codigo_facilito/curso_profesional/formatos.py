texto = "  curso de Python  "

resultado_uno = texto.capitalize()#crea una nueva cadena de caracteres con la primer letra en mayusculas
resultado_dos = texto.swapcase()#pasar las mayusculas a minusculas y viceversa
resultado_tres = texto.upper()  #pasar todas las letras a mayusculas
resultado_cinco = texto.title()#da un formato de titulo 
resultado_cuatro = texto.replace("Python", "Ruby")#remplazzas una parte de la cadena por otra (vieja,nueva,numero de veces que se sustituira)
resultado_seis = texto.strip()#quita los espacios antes o despues de la cadena

print(resultado_uno)
print(resultado_dos)
print(resultado_tres)
print(resultado_tres.isupper()) #para preguntar si la cadena son mayusculas
print(resultado_dos.islower())  #para preguntar su la cadena son minusculas
print(resultado_cinco)
print(resultado_cuatro)
print(resultado_seis)