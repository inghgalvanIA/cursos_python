def suma(val_uno,val_dos,val_tres):
    return val_uno + val_dos + val_tres

def curso():
    return "Curso de Python", "basico", 3.7

nuevo_valor = suma(15,22,33)
print(nuevo_valor)

curso, nivel, version = curso()
print(curso,nivel,version)