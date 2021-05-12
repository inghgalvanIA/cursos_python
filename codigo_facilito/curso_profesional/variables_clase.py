class Circulo:
 
    sepi = 3.1416 #es una variable de clase

def __init__ (self,radio):
    self.radio = radio #es una variable de instancia

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100

print(Circulo.pi)
print(circulo_b.radio)
print(circulo_a.radio)