class Triangulo:
    numero = 2 #variable de clase

    @staticmethod
    def area(base,altura):
        return(base * altura) / Triangulo.numero

resultado = Triangulo.area(10,20)
triangulo_dos = Triangulo.area(23,30)
print(resultado)
print(triangulo_dos)