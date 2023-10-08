"""
Exercício 1: Criar uma Classe Básica
Crie uma classe chamada Pessoa com atributos como nome e idade. Defina um método para imprimir os detalhes da pessoa.
"""

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return(self.nome)+ "-" + str(self.idade)
    
    def __eq__(self, outro):
        if isinstance(outro, Pessoa):
            return self.nome == outro.nome and self.idade == outro.idade
        return False 

p1 = Pessoa("yann", 19)
pCopia = Pessoa("yann", 19)
p2 = Pessoa("Bipe", 47)
p3 = Pessoa("Giuliana", 18)

lista_pessoas = []
lista_pessoas.append(p1)
lista_pessoas.append(p2)
lista_pessoas.append(p3)

for x in range(len(lista_pessoas)):
    print(lista_pessoas[x])


print(p1 == pCopia)
print(p1 is pCopia)