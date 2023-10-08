def criar_dicionario(texto):
    palavras = texto.split()
    dicionario_resultante = {}

    for palavra in palavras:
        palavra_sem_espaco = palavra.replace(" ", "")
        dicionario_palavra = {
            "cont" : palavras.count(palavra),
            "hist" : {}
        }

        for letra in palavra_sem_espaco:
            if letra in dicionario_palavra["hist"]:
                dicionario_palavra["hist"][letra] += 1
            else:
                dicionario_palavra["hist"][letra] = 1

        dicionario_resultante[palavra] = dicionario_palavra
    return dicionario_resultante

texto = input("Digite o texto: ")
dicionario_final = criar_dicionario(texto)
print(dicionario_final)