"""
Escreva um programa que solicite ao usuário um número inteiro e calcule a soma de seus dígitos. Use um loop while para extrair os dígitos
"""
num = int(input("Digite um número inteiro: "))
soma = 0
while num > 0:
    soma += num % 10
    num = num // 10
print(f"soma: {soma}")