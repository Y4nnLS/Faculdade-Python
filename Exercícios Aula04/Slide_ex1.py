"""
try:
    num = int(input("Digite um número inteiro: "))
except ValueError:
    print("dado invalido")
"""
senha = 1234
tentativa = 0
while tentativa < 3:
    try:
        op = int(input("Digite sua senha: "))
        tentativa += 1
    except ValueError:
        print("Tipo de senha inválida")
        tentativa += 1
    else:
        if op == senha:
            print("Acesso permitido...")
            break
        else:
            print("Acesso negado")
    
print("Encerrando o programa...")

