def valida_string(str, min, max):
    tamanho = len(str)
    return min <= tamanho <= max

print(valida_string("cu", 1, 3))