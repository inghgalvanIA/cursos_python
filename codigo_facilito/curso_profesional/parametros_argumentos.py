def crear_usuario(nombre,apellido,edad):
    return{
        "nombre":nombre,
        "apellido":apellido,
        "nombre_comleto":"{}{}".format(nombre,apellido),
        "edad":edad
    }
codi = crear_usuario("Codi","Facilito",7)

print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])