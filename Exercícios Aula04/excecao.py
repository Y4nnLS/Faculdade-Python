try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Erro de divisão por zero")
else:
    print(f"Resultado {resultado} {type(resultado)}")
finally:
    print("Encerrando o programa...")