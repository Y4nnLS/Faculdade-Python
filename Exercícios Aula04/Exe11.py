"""
Crie uma exceção personalizada chamada EstoqueInsuficienteErros. Implemente uma classe PRODUTO que tenha um nome e uma quantidade em estoque.
Crie um método VENDER que aceite a quantidade desejada como argumento e lance a exceção.
EstoqueInsufucienteError se a quantidade for maior que o estoque disponível.
"""
class EstoqueInsuficienteError(Exception):
    def __init__(self, produto, quantidade_vendida):
        self.produto = produto
        self.quantidade_vendida = quantidade_vendida
        self.mensagem = f"Estoque insuficiente para vender {quantidade_vendida} unidades de {produto.nome}."
class Produto:
    def __init__(self, nome, estoque):
        self.nome = nome
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade > self.estoque or quantidade < 0:
            raise EstoqueInsuficienteError(self, quantidade)
        self.estoque -= quantidade
        print(f"{quantidade} unidades de {self.nome} vendidas. Estoque restante: {self.estoque}")
produto = Produto("caneta", 20)
try:
    quantidade_venda = int(input("Quantas unidades você deseja comprar: "))
    produto.vender(quantidade_venda)
except EstoqueInsuficienteError as e:
    print("Erro: ", e.mensagem)