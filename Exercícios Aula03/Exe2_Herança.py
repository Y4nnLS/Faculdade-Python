"""
Exercício 2: Herança
Crie uma classe base chamada Animal com um método fazer_som(). 
Em seguida, crie duas classes derivadas, como Cachorro e Gato, que herdem da classe Animal e tenham seus próprios sons.
"""

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"Nome = {self.nome}, Idade = {self.idade}, Classe = {self.__class__}"


class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def fazer_som(self):
        print("AuAu")

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def fazer_som(self):
        print("Meow")

a1 = Gato("Luna", 5)
c1 = Cachorro("Dolly", 7)
g1 = Gato(idade = 4, nome="Pimenta")

print(a1)
a1.fazer_som()
print(c1)
c1.fazer_som()
print(g1)
g1.fazer_som()