print("ingresa la calificacion del alumno")

calificacion = int(input())
color = None

if calificacion >= 7 :
    color = "verde"
else:
    color = "rojo"
print ("la calificacion ",calificacion,"es ", color)

