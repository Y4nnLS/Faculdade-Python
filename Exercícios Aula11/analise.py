import csv
import time

nulo = 'VOTO NULO'
branco = 'VOTO BRANCO'

with open("C:\Programação\Python\Faculdade\Exercícios Aula10\\votacao_secao_2022_PR.csv", "r", encoding='latin-1') as arq:
    csv_leitor = csv.DictReader(arq)

    ini = time.time()

    lista = []
    for linha in csv_leitor:
        if linha['DS_CARGO'] == 'GOVERNADOR' and linha['NM_VOTAVEL'] not in(nulo,branco):
            lista.append(linha['NM_VOTAVEL'])
    govs_nomes = set(lista)

    fim = time.time()

    print(len(govs_nomes),govs_nomes)
    print(f"*** TESTE 1: {fim-ini} segundos")