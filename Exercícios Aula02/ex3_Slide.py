"""
Crie uma lista vazia para representar uma lista de compras. Peça ao usuário para adicionar itens à lista até que ele digite "fim". Em seguida, exiba a lista de compras.
"""
lista = []
while True:
    produto = input("Digite o nome do produto que deseja adicionar na lista: ")
    if(produto.lower() == "fim"):
        break
    lista.append(produto)

print(lista)