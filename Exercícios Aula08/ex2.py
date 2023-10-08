estoque = dict()
print(estoque)
estoque['banana'] = 20

estoque['whey'] = 3

estoque['cretina'] = 2

print(estoque)

estoque['banana'] = 10
print(estoque)

estoque.pop('whey')
print(estoque)