"""
Crie uma exceção personalizada chamada ValorInvalidoErros. Crie uma função que recebe um número como entrada e lança esse exceção se o número for negativo.
"""
class ValorInvalidoError(Exception):
    pass
try:
    valor = int(input("Digite um número: "))
    if valor < 0 or valor > 1000000:
        raise ValorInvalidoError()
except ValueError:
    print("Digite um valor inteiro")
except ValorInvalidoError:
    print("Digite um valor entre 0 e 1000000")
else:
    print(f"Número: {valor}")
