def recebe_string(palavra):
    for letra in palavra:
        contador[letra] = contador.get(letra, 0) + 1

contador = {}
palavra = input("digite uma palavra: ")
recebe_string(palavra)
for chave, valor in contador.items():
    print(f"{chave}: {valor}")
    