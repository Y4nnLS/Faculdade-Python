lista = []
for i in range(100):
    lista.append(0)
print(lista)

lista1 = [0] * 100
print(lista1)

lista2 = [1]*100
print(lista2)

lista3 = [0, 1] * 200
print(lista3)

lista4 = [ x + 5 for x in lista3]
print(lista4)

lista5 = [ x ** 2 for x in lista4]
print(lista5)

lista6 = lista5.copy()
for i in lista6:
    lista6.remove(25)
print(lista6)

lista7 = lista5.copy()
lista8 = [x for x in lista7 if x != 25]
print(lista8)