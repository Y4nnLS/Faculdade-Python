import random
import math

class ValorInvalidoError(Exception):
    pass

def le_valor_int(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor < 0 or valor > 1000000:
                raise ValorInvalidoError()
        except ValueError:
            print("Digite um valor inteiro")
        except ValorInvalidoError:
            print("Digite um valor entre 0 e 1000000")
        else:
            return valor

while True:
    n1 = le_valor_int("Digite o valor inicial: ")
    n2 = le_valor_int("Digite o valor final: ")
    break

numero=random.randint(n1, n2)


print(f"{numero}")
tentativas = math.ceil(math.log2(n2 - n1))
print(f"numero de tentativas:{tentativas}")
while tentativas > 0:
        tentativa = le_valor_int("Faça sua tentativa: ")
        print("Tipo de valor inválido")
        tentativas -= 1
        if tentativa == numero:
            print("Você ganhou!!")
            break

        if tentativa < numero:
            print(f"{tentativa} é menor do que o sorteado")

        else:
            print(f"{tentativa} é maior do que o sorteado")
else:
    print("Excedeu o número de tentativas...")
print("Finalizando o programa...")
