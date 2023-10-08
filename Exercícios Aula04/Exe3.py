"""
Crie uma função que leia um arquivo e retorne seu conteúdo. Trate exceções caso o arquivo não seja encontrado.
"""
arquivo = "lista_palavras.txt" 
def le_arquivo(arq):
    try:
        with open(arq, encoding="UTF-8") as f:
            return [linha.strip() for linha in f]
    except FileNotFoundError:
        print("Arquivo não encontrado...")

lista = le_arquivo(arquivo)
print(lista) 