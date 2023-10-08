import csv

file_path = r"C:\Programação\Python\Faculdade\Exercícios Aula10\chamada.txt"
output_path = r"C:\Programação\Python\Faculdade\Exercícios Aula10\chamadaPresente.txt"

colunas = [["nome"],["n1"],["n2"]]

with open(file_path, encoding="UTF-8") as f:
    with open(output_path, "a", encoding="UTF-8") as arq:
        with open("C:\Programação\Python\Faculdade\Exercícios Aula10\chamadanotas.csv", "a", encoding="UTF-8", newline="") as arqcsv:
            for linha in f:
                print(linha, end="")
                presenca = input("Presente - (S/N): ")
                arq.write(f"{linha.strip()} - presente: {presenca.upper()}\n")
                if presenca == 'S':
                    csv_escritor = csv.writer(arqcsv)
                    csv_escritor.fieldnames = colunas
                    n1 = float(input(f"Digite a nota 1 do aluno {linha}: "))
                    n2 = float(input(f"Digite a nota 2 do aluno {linha}: "))
                    csv_escritor.writerow([linha, n1, n2])
