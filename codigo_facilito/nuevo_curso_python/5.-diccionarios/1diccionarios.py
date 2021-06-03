"""
los diccionarios es una estructura de datos que almacena diferentes tipos de datos
los diccionarios son mutables (agregar o modificar su longitud)
los diccionarios se rigen con la relacion llave:valor
una llave puede ser cualquier tipo-dato

diccionario = {"llave_uno":"valor_uno","llave_dos":"valor_dos"}
"""

ejemplo_diccionario = {"Total":55,10:"Curso de Python",(1,2,3):True}
dic_alumnos = {"Eduardo":1,"Fernando":2,"Carlos":3}
print(ejemplo_diccionario)

#creaacion del diccionario con dict
diccionario = dict()

#agregar nueva llave valor
diccionario["usuario"] = "Eduardo"
print(diccionario)

#actualizar valor mediante una llave 
diccionario["usuario"] = "eduardo_gpg"
print(diccionario)

#obtener valor mediante una llave
print(diccionario["usuario"])

#obtener todas las llaves del diccionario
llaves = ejemplo_diccionario.keys()
print(llaves)

#obtener todos los valores del diccionario
valores = ejemplo_diccionario.values()
print(valores)

#imprimir los valores con for
for key, value in dic_alumnos.items():
    print(key,value)