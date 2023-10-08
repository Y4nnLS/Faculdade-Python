"""
Exercício 4: Polimorfismo
Crie uma classe FormaGeometrica com um método calcular_area().
Crie classes derivadas como Retangulo e Circulo que implementem esse método de maneira diferente para cada uma.
"""
import math

class FormaGeometrica:
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
            return(self.base * self.altura)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
         return math.pi * self.raio ** 2

r1 = Retangulo(10, 20)
print(f"Área do Retângulo: {Retangulo.calcular_area(r1)}")
c1 = Circulo(2)
print(f"Área do Circulo: {Circulo.calcular_area(c1)}")