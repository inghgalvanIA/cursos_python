class Triangulo:
    def area(self):
        return(self.base * self.altura)/2

#crear una instancia
triangulo = Triangulo()
triangulo.base = 10
triangulo.altura = 20

resultado = triangulo.area()
print(resultado)