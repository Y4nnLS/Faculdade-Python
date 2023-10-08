l1 = [1,2,3,4, 5, 6]
l1_quad = [x ** 2 for x in l1]
l1_quad.clear()

for x in l1:
    l1_quad.append(x**2)
print(l1_quad)

l1_quad.clear()

def quadrado(n):
    return n**2

l1_quad = list(map(quadrado, l1))

def soma(x, y):
    return x + y

l2 = [-1,-2,-3,-4,-5]
l3 = list(map(soma,l1, l2))
print(l3)

l1_pares = [x for x in l1 if x % 2 == 0]
print(l1_pares)
# l1_pares = list(filter(, l1))