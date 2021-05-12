calificaciones = {"biologia":8,"quimica":9,"español":8,"matematicas":10,"civismo":9}

biologia = calificaciones["biologia"]
quimica  = calificaciones["quimica"]
español  = calificaciones["español"]
matematicas = calificaciones["matematicas"]
civismo = calificaciones["civismo"]

promedio = (biologia + quimica + español + matematicas + civismo)/5

print(calificaciones)
print(promedio)

if matematicas > biologia:
    print ("la mayor calificacion es ",matematicas)
else:
    print ("la mayor calificacion es ",biologia)