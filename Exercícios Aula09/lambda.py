from functools import reduce
# lambda argumentos: expressao
teste = lambda x, y: x + y

print(teste(10,12))

l3 = ['arara', 'banana', 'aaooaa', 'papa']
lista3 = list(filter(lambda palavra: palavra == palavra[::-1], l3))
print(lista3)

# reduce(funcao, iteravel)
# reduz a um unico valor/objeto

l1 = [1,2,3,4,5]
def soma(x, y):
    return x + y
soma1 = reduce(soma, l1)
print(soma1)

# ex concatenar uma lista de strings:
palavras = ['a','e', 'i', 'o', 'u']

vogais1 = reduce(lambda x, y: x + y, palavras)
print(vogais1)

# em uma linha:
l_final = [4,61,3,4,6,7,8]
# l_res sendo a soma dos quadrados dos pares l_final

l_res = reduce(lambda x, y: x + y,map(lambda x: x**2,filter(lambda x : x % 2 == 0, l_final)))
print(l_res)