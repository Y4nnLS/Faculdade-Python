import random

def menu():
    print("+-------------------------------+")
    print("| Bem vindo(a) ao jogo da forca |")
    print("+-------------------------------+")

def escolhe_palavra():
    arquivo = open("C:\Programação\Python\Faculdade\Forca\lista_palavras.txt", "r", encoding="UTF-8")
    palavras = []
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()
    palavra_secreta = numero_letras(palavras)
    print(palavra_secreta)
    return palavra_secreta
    
def numero_letras(palavras):
    num_letras = int(input("Digite o numero de letras da palavra secreta: "))
    palavra_x_letras = []
    [palavra_x_letras.append(x) for x in palavras if int(len(x)) == num_letras]
    if(len(palavra_x_letras) == 0):
        print("Não existe palavras com a quantidade de caracteres especificados, escolhendo palavra aleatória...")
        numero_palavra = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero_palavra].upper()
        return palavra_secreta
    else:
        print("Escolhendo uma palavra...")
        palavra = random.choice(palavra_x_letras)
        return palavra

def encerra_programa():
    input("Para encerrar o programa aperte ENTER")
    clear()

def clear():
    try: 
       import os
       os.system("cls")
    except AttributeError:
        print()

def adiciona_palavra():
    f = open("lista_palavras.txt", "a")
    palavra = input("Digite uma palavra: ")
    palavra = palavra.strip().lower()
    f.write("\n{}".format(palavra))
    f.close()

def inicializa_letras_corretas(palavra):
    return ["_" for letra in palavra]

def recebe_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def verifica_chute(palavra_secreta, chute, letras_corretas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_corretas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    menu()
    palavra_secreta = escolhe_palavra()
    letras_corretas = inicializa_letras_corretas(palavra_secreta)
    print(letras_corretas)

    enforcou = False
    acertou = False
    erros = 0
    
    while(not enforcou and not acertou):
        chute = recebe_chute()

        if(chute in palavra_secreta):
            verifica_chute(palavra_secreta, chute, letras_corretas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_corretas
        print(letras_corretas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    
    opc = input("Você deseja adicionar uma nova palavra? (S|N)")
    opc = opc.strip().upper()
    if(opc == "S"):
        adiciona_palavra()
        encerra_programa()
    else:
        encerra_programa()

if(__name__ == "__main__"):
    jogar()