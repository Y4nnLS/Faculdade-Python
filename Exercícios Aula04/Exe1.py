"""
Crie um programa que solicite ao usuário um número inteiro e, se o usuário digitar algo que não seja um número, trate a exceção.
"""
try:
    num = int(input("Digite um número inteiro: "))
except ValueError:
    print("Valor inválido")