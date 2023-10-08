def recebe_string(palavra):
    for letra in palavra:
        contador[letra] = contador.get(letra, 0) + 1

contador = {}
palavra = "banana" # input("digite uma palavra: ")
recebe_string(palavra)
print(f"Dicionario:\n{contador}")

for chave, valor in contador.items():
    print(f"{chave}: {valor}")

contador_invertido = {valor: chave for chave, valor in contador.items()}
print(f"\nDicionario Invertido\n{contador_invertido}")
for chave, valor in contador_invertido.items():
    print(f"{chave}: {valor}")