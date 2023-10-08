import csv

with open("C:\Programação\Python\Faculdade\Exercícios Aula10\pessoa.csv", encoding="UTF-8") as f:
    csv_leitor = csv.reader(f) # instância para leitura
    next(csv_leitor) # next() pula linha
    for linha in csv_leitor:
        print(linha[0])

pessoa = [["giu"],[19],["brasil"]]
with open("C:\Programação\Python\Faculdade\Exercícios Aula10\pessoa.csv", "a", encoding="UTF-8", newline="") as arq:
    csv_escritor = csv.writer(arq, delimiter=",") # instância para escrita
    """
    escrita do cabeçalho

    csv_escritor.writerow(colunas)
    """
    # escrita dos valores
    for linha in pessoa:
        csv_escritor.writerow(pessoa)