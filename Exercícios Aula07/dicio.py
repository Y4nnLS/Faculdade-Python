pessoa = dict()
pessoa['nome'] = 'Alexandre'
pessoa['idade'] = 29
pessoa['cidade'] = 'Curitiba'
print(pessoa)
print()
for chave in pessoa:
    print(f"{chave}:{pessoa[chave]}")