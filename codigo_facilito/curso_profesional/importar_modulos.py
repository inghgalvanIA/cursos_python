#forma de importar modulos
# import calculadora

# resultado = calculadora.suma(10, 20)
# print(resultado)
##########################################

#importar todos las funciones
#from calculadora import *

##########################################

#renombrar la funcion que estamos importando
#from calcuradora import suma as nueva_suma


#importar varios modulos
from calculadora import (suma,
                         resta,
                         multiplicacion)


resultado = suma(10,20)
resultado_resta = resta(10,20)
resultado_mult = multiplicacion(10, 20)

print(resultado)
print(resultado_resta)
print(resultado_mult)