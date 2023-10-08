"""
 {} | {} | {} | {}
----+----+----+----
 {} | {} | {} | {}
----+----+----+----
 {} | {} | {} | {}
----+----+----+----
 {} | {} | {} | {}
"""
# da pra usar dicionario para montar (0,0) : 'X' (0,1) : ' _ ' (0,2) : 'O'
tabuleiro = [   [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]
            ]

def imprime_tabuleiro():
    for casa in tabuleiro:
        print(f"{casa}", end="\n")

def ganhou():
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] == linha[3] != 0:
            return True
    for coluna in range(4):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == tabuleiro[3][coluna] != 0:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3] != 0:
        return True
    if tabuleiro[0][3] == tabuleiro[1][2] == tabuleiro[2][1] == tabuleiro[3][0] != 0:
        return True
    return False
    
jogada = 0

while True:
    print(f"Jogador {jogada%2 + 1}")
    imprime_tabuleiro()
    jogador = input("Digite a coordenada da sua jogada[linha][coluna]: ")
    linha,coluna = [int(posicao) for posicao in jogador.split()]
    linha = int(linha)
    coluna = int(coluna)
    
    print(jogada)
    if tabuleiro[linha-1][coluna-1] == 0:
        if(jogada%2+1) == 1:
            tabuleiro[linha-1][coluna-1] = 'X'
        else:
            tabuleiro[linha-1][coluna-1] = 'O'
    else:
        print("Não está vazio")
        jogada -=1
    
    jogada += 1
    if ganhou():
        imprime_tabuleiro()
        print("ganhou")
        break