lista1 = []
for i in range(999, 200, -2):
    lista1.append(i)
print(f"1000 a 200: {lista1}\n")

lista2 = []
for i in range(203, 1000, 7):
    lista2.append(i)
print(f"Multiplo de 7 de 200 a 1000: {lista2}\n")

lista3 = []
for i in range(504, 5000, 21):
    lista3.append(i)
print(f"Multiplo de 7 e 3 de 500 a 5000: {lista3}\n")

for i in lista3:
    if i % 5 == 0:
        lista3.remove(i)
        del i #também funciona

print(f"Lista anterior, sem os múltiplos de 5: {lista3}\n")