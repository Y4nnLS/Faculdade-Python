pontos = 0
def joga_dados():
    import random
    return random.randint(2, 12)
    
def rodada1(dados):
    if dados == 7 or dados == 11:
        print("Natural - Você ganhou")
    elif dados == 2 or dados == 3 or dados == 12:
        print("Craps - Você perdeu")
    else:
        print("Ponto")
        pontos = dados
        rodadas(joga_dados(), pontos)

def rodadas(dados, pontos):
    print(f"Valor dos dados: {dados}")
    if dados == 7:
        print("Você perdeu")
    elif dados == pontos:
        print("Você ganhou")
    else:
        dados = joga_dados()
        rodadas(joga_dados(), pontos)

rodada = 1
dados = joga_dados()
print(f"Valor dos dados: {dados}")
if rodada == 1:
    rodada +=1
    rodada1(dados)
else:
    rodadas(dados)

