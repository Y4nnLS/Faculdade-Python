# Filtre os elementos que são múltiplos de 3 e 5 ao mesmo tempo
l2 = [2,5,15,342,45,32,30]
def l2_3_5(n):
        return n % 3 == 0 and n % 5 == 0

lista2 = list(filter(l2_3_5,l2)) 
print(lista2)

# Filtre os elementos que são palíndromos
l3 = ['arara', 'banana', 'aaooaa', 'papa']
def verifica_palindromo(palavra):
    return palavra == palavra[::-1]
lista3 = list(filter(verifica_palindromo, l3))
print(lista3)
# Filtre as pessoas com idade maior que 30 do sexo feminino
d = {'andrea':
    {
        'idade': 40,
        'sexo' : 'f'
    },
    'jose':
    {
        'idade': 39,
        'sexo' : 'm'
    },
    'maria':
    {
        'idade': 50,
        'sexo' : 'f'
    },
}
def verifica_idade_sexo(elemento):
      return elemento[1]['idade'] > 30 and elemento[1]['sexo'] == 'f'
lista_d = dict(filter(verifica_idade_sexo,d.items()))
print(lista_d)