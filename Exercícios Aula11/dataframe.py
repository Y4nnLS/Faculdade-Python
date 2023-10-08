import pandas as pd

dicio = {
    'nome' : ['alex','bipe','yann'],
    'idade': [20, 18, 19],
    'cidade' : ['curitiba', 'pau grosso do sul', 'japao']
}

df = pd.DataFrame(dicio)
df.index = ['p1','p2','p3']
print(df)

# informações
print(df.info())
# dimensões
print(df.shape)
# colunas
print(df.columns)
# indices de linha
print(df.index)
# acesso a coluna
print(df['nome'])
print(df['idade'])
# acesso a linha
print(df.loc['p1'])