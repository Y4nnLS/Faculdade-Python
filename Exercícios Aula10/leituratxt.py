"""
f = open("C:\Programação\Python\Faculdade\Exercícios Aula10\\votacao_10000linhas.csv", "r", encoding="UTF-8")
for linha in f:
    print(linha)

f.close()
"""

"""
outra maneira de abrir.
A vantagem é que ele abre e fecha o arquivo, dentro do escopo do with

with open("C:\Programação\Python\Faculdade\Exercícios Aula10\votacao_10000linhas.csv", encoding="UTF-8") as arq:
    for linha in arq:
        print(linha)
"""
# w - sobreescreve
# a - append
with open("C:\Programação\Python\Faculdade\Exercícios Aula10\presentes.txt", "a", encoding="UTF-8") as arq:
    for i in range(11):
        arq.write(str(i))