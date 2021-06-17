"""

los callbacks son funciones las cuales son utilizadas como argumentos 
para otras funciones, y seran las funciones que reciben estos argumentos que las llamen 

"""

promedio = lambda *args : sum(args) / len(args) 

aprobatorio = lambda calificacion : calificacion >= 7

def mostrar_mensaje(fun_promedio,fun_aprobatorio,*args):
    #se pone *args para no pasarlo en formato tupla
    promedio = fun_promedio(*args)

    if fun_aprobatorio(promedio):
        print(f"Felicidades, aprobaste la materia con {promedio}")
    else:
        print("no aprobaste la materia ")

mostrar_mensaje(promedio,aprobatorio,10,10,9,8,7)