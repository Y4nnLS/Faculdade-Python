def recebe_string(palavra):
    fruta = dict()
    ID = 0
    for i in range(palavra):
        ID += 1
        fruta[i] = ID
    return fruta


dicionario = recebe_string(input("banana"))
# print({chave}: {})