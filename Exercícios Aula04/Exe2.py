"""
Escreva uma função que divida dois números, tratando a exceção caso a divisão por zero ocorra.
"""
def divisao(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erro: Divisão por Zero")
    else:
        return result

print(divisao(10,0))