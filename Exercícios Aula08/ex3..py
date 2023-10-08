dicionario = {
    'hello' : 'ola',
    'world' : 'mundo',
    'green' : 'verde'
}

palavra = input("Digite a palavra que deseja traduzir: ")
if palavra in dicionario:
    print(f'{dicionario[palavra]}')