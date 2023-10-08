nomes = ['Alex', 'Jenifer', 'Maria', 'João']

def nome_M(nome):
    return nome.upper()
nomes_maiusculo = list(map(nome_M, nomes))
nomes_maiusculo = list(map(str.upper, nomes))

print(nomes_maiusculo)