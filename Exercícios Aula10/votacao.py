import csv

with open("C:\Programação\Python\Faculdade\Exercícios Aula10\\votacao_10000linhas.csv") as f:
    csv_leitor = csv.reader(f)
    next(csv_leitor)
    for linha in csv_leitor:
        if linha[-6] == "GOVERNADOR" or linha[-6] == "DEPUTADO ESTADUAL":
            if linha[-4] == "VOTO BRANCO" or linha[-4] == "VOTO NULO":
                continue
            print(F"{linha[-4]} - {linha[-1]}")