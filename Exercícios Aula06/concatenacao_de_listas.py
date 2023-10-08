comidas = ['banana', 'carne', 'maça', 'chocolate', 'cereja']
bebidas = ['leite', 'agua']

# concatenação
comidas += bebidas
comidas += ['suco']
print(comidas)

# concatenação múltipla
comidas = comidas * 3
print(comidas)

# slice
print(comidas[:3])
print(comidas[1:5])
print(comidas[1:5:2])

# índices negativos
print(comidas[-1]) # -1 acessa a última posição
print(comidas[-2:-5:-1])

# atribuição em intervalo
lista_letras = ["alex","joao","maria"]
print(lista_letras)

# inserir bruno e eduardo
lista_letras[1:1] = ["bruno","eduardo"]
print(lista_letras)
lista_letras.append("maciel")
print(lista_letras)

lista_letras.sort(reverse=True)
print(lista_letras)

# referência e cópia
lista2 = comidas
lista3 = comidas.copy()
lista4 = comidas[:]

print(id(comidas),id(lista2),id(lista3),id(lista4) )

comidas.extend(bebidas)
print(comidas)

comidas.sort()
print(comidas)

comidas.reverse()
print(comidas)

mercado = comidas + bebidas
print(mercado)

print(mercado.count('leite'))
print(mercado.index('leite'))
