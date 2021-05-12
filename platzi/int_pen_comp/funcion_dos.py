def nombre_completo (nombre, apellido, inverso=False):
    if inverso:
        return f"{apellido} {nombre}"
    else:
        return f"{nombre}{apellido}"

print(nombre_completo ("Héctor","Galván",inverso=True))