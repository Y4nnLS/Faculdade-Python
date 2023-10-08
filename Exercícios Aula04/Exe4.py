"""
Implemente um programa de calculadora que solicite ao usuário uma operação e dois números, realizando o cálculo e tratando exceções apropriadas.
"""
try:
    x, y, op = input("Digite dois números e o operador matemático(por último), separados por ponto-vírgula: ").split(";")
    x = int(x)
    y = int(y)

except ValueError:
    print("Valor inválido")
else:
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

