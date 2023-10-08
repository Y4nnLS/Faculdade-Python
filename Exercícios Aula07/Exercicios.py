"""
Gere uma lista de números pares de 0 a 20 utilizando list comprehension
"""
numeros_pares = [x for x in range(0,21) if x%2 == 0]
print(f"Pares de 0 a 20: {numeros_pares}")

"""
Crie uma lista com os cubos dos números de 1 a 10 utilizando list comprehension
"""
cubo_numeros = [x ** 3 for x in range(1, 11)]
print(f"Cubo de 1 a 10: {cubo_numeros}")

"""
Dada uma lista de números, crie uma nova lista contendo apenas os números ímpares da lista original
"""
lista_numeros = [1,2,3,4,5,6,7,8,9,10,3,4,5,6,8]
nova_lista_numeros = [x for x in lista_numeros if x % 2 == 1]
print(f"Nova lista com os ímpares: {nova_lista_numeros}")

"""
Dada uma lista de strings, crie uma nova lista contendo apenas as strings com mais de 5 caracteres
"""
lista_strings = ["aba","teste", "yann", "morango", "borboleta", "rosa", "python", "programador", "desenvolvedor", "anilina"]
nova_lista_strings = [palavra for palavra in lista_strings if len(palavra) > 5]
print(f"Nova lista strings: {nova_lista_strings}")

"""
Dada uma lista de números, encontre o segundo maior número
"""
print(f"Segundo maior número: {lista_numeros[-2]}")

"""
Dada uma lista de strings, ordene-a em ordem alfabética
"""
lista_strings.sort()
print(f"Lista de string em ordem alfabética: {lista_strings}")

"""
Crie uma função que recebe uma lista de números e retorna a lista sem elementos repetidos
"""
def remove_repetidos(lista_numeros):
    lista = []
    for numero in lista_numeros:
        if numero not in lista:
            lista.append(numero)
    return lista
print(f"Lista números sem repetidos: {remove_repetidos(lista_numeros)}")

"""
Implemente uma busca binária em uma lista ordenada
"""
numero_procurado = 1

def busca_binaria(lista, numero_procurado):
    tamanho_lista = len(lista)
    inicio = 0
    fim = tamanho_lista-1
    while inicio <= fim:
        meio = (inicio+fim) // 2
        if lista[meio] == numero_procurado:
            return meio
        elif lista[meio] < numero_procurado:
            inicio = meio + 1
        elif lista[meio] > numero_procurado:
            fim = meio - 1
    return False
posicao = busca_binaria(lista_numeros, numero_procurado)
print(f"o numero {numero_procurado} está na posição {posicao}")

"""
Crie uma função para inverter uma lista sem usar métodos internos como reverse()
"""
def inverte_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida
print(f"Lista invertida: {inverte_lista(lista_numeros)}")

"""
Dada uma lista de palavras, crie uma função que retorna uma nova lista contendo apenas as palavras palíndromas(que se leem da mesma forma de trás para frente)
"""
def verifica_palindromo(lista_palavras):
    lista_palindromos = []
    for palavra in lista_palavras:
        inverso = palavra[::-1]
        if inverso == palavra:
            lista_palindromos.append(palavra)
    return(lista_palindromos)
print(f"Lista de palindromos: {verifica_palindromo(lista_strings)}")