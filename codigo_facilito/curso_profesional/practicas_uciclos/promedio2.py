calificaciones = {"biologia":8,"quimica":9,"español":8,"matematicas":10,"civismo":9}

lista = calificaciones.values()
lista = list(lista)

promedio = (lista[0] + lista[1] + lista[2] + lista[3] + lista[4])/5
mejor    = max(lista)

print(lista)
print("el promedio de las calificaciones es:", promedio)
print("la materia con mejor promedio es: ", mejor)