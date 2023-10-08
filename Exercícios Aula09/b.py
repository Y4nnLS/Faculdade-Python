def calc_media(*notas):
    return sum(notas) / len(notas)

n1 = [4.5,6.7,3.4,2.1,9.9]
n2 = [8.8,4.5,2.3,1.9,5.6]
n3 = [7.6,3.7,3.2,5.5,3.2]

media = list(map(calc_media, n1, n2, n3))
print(media)