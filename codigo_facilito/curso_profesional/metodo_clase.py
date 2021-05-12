class Circulo:
    pi = 3.1416


@classmethod
def area(cls, radio):
    return cls.pi * radio**2

resultado = Circulo.area(10)
print(resultado)