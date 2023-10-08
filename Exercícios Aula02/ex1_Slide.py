"""
Crie um programa que pede ao usuário dois números e uma operação matemática(+,-,*,/). O programa deve realizar a operação escolhida e exibir o resultado.
"""
x, y, op = input("Digite dois números e o operador matemático(por último), separados por ponto-vírgula: ").split(";")
x = int(x)
y = int(y)
match op:
    case "+":
        print(f"{x} + {y} = {x + y}")
    case "-":
        print(f"{x} - {y} = {x - y}")
    case "/":
        print(f"{x} / {y} = {x / y}")
    case "*":
        print(f"{x} * {y} = {x * y}")
    case _:
        print("Operador inválido")