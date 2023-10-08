"""
Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela
de códigos a seguir para obter o preço de cada produta:
Código Preço
1       0,50
2       1,00
3       4,00
5       7,00
9       8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de "Código inválido".
"""

def tabela_de_codigos():
    print("Código Preço")
    print("1       0,50")
    print("2       1,00")
    print("3       4,00")
    print("5       7,00")
    print("9       8,00")
op = 1
total = 0.0
while op != 0:
    tabela_de_codigos()
    op = int(input("Digite o código do produto: "))
    match op:
        case 1:
            total += 0.50
        case 2:
            total += 1
        case 3:
            total += 4
        case 5: 
            total += 7
        case 9:
            total += 8
        case 0:
            break
        case _:
            print("Código inválido")
print('Total das compras: R$ %.2f'% (total))