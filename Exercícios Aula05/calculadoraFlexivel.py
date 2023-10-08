class FaltaOperandosError(Exception):
    pass

def verifica_operandos(*numeros):
    if len(numeros) < 2:
        return False if len(numeros) < 2 else True
        

def calculadora_flex(operador, *numeros):
    res = 0
    
    match operador:
        case "soma":
            for numero in numeros:
                res = sum(numeros)
            return res
        case "sub":
            if len(numeros) < 2:
                return ValueError("Erro na função, faltando operandos")    
            for numero in numeros:
                res = numeros[0] - sum(numeros[1:])
            return res
        case "mult":
            res = 1
            for numero in numeros:
                res *= numero
            return res
        case "div":
            if len(numeros) < 2:
                return ValueError("Erro na função, faltando operandos")
            res = numeros[0]/ numeros[1]
            for numero in numeros[2:]:
                res /= numero
            return res
        case _:
            return("Inválido...")

print(calculadora_flex("soma", 4, 5, 6, 7))
print(calculadora_flex("soma", 4, 5))
print(calculadora_flex("sub", 10, 8, 2))
print(calculadora_flex("sub", 10))
print(calculadora_flex("mult", 3, 4))
print(calculadora_flex("mult", 3, 4, 2))
print(calculadora_flex("div", 4, 3))
print(calculadora_flex("div", 4, 3, 2))