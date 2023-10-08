lista1 = []
lista2 = []
lista_pares = []
lista_impares = []
    
for i in range(1, 101):
    lista1.append(i)
    lista2.insert(i-1,i)
    if i % 2 == 0:
        lista_pares.append(i)
    else: 
        lista_impares.append(i)

print(f"Lista1 de 1 a 100: {lista1}\n")
print(f"Lista2 de 1 a 100: {lista2}\n")
print(f"Lista_pares de 1 a 100(pares): {lista_pares}\n")
print(f"Lista_impares de 1 a 100(impares): {lista_impares}\n")

