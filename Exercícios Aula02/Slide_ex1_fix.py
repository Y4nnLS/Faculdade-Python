"""
Desenvolva um jogo em que o programa seleciona um número aleatório entre 1 e 100, e o jogador tenta adivinhar qual é o número.
O programa deve fornecer dicas se o palpite for muito alto ou muito baixo.
Use um loop while para permitir várias tentativas.
"""
import random
tentativas = 7
num_secreto = random.randint(1, 101)
print(num_secreto)
while tentativas > 0:
    tentativas -= 1
    try:
        num = int(input("Digite o número: "))
    except ValueError:
        print("Valor inválido")
    else:
        if num == num_secreto:
            print("Você ganhou")
            break
        elif num > num_secreto:
            print(f"{num} é maior que o número secreto")
        else:
            print(f"{num} é menor que o número secreto")