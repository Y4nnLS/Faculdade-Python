"""
Peça ao usuário para digitar a quantidade de notas que deseja calcular.
Em seguida, peça as notas e calcule a média. No final, exiba a média. Use um loop for para ler as notas e calcular a média
"""
quant_notas = int(input("Digite a quantidade de notas que deseja calcular: "))
soma = 0
for i in range(quant_notas):
    nota = float(input("Digite a nota: "))
    soma += nota
media = soma / quant_notas
print(f"A média das notas é igual a {media}")