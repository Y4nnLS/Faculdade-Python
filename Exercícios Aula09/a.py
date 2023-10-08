n1 = [4.5,6.7,3.4,2.1,9.9]
n2 = [8.8,4.5,2.3,1.9,5.6]
n3 = [7.6,3.7,3.2,5.5,3.2]

def calcula_media(n1, n2, n3):
    return ((n1 + n2 + n3) / 3)

media = list(map(calcula_media, n1, n2, n3))
print(media)