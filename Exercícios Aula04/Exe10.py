"""
Crie uma exceção personalizada chamada SenhaFracaError. Escreva uma função que verifica se uma senha possui pelo menos 8 caracteres e pelo menos um caractere numérico.
Se a senha não atender a esses critérios, lance a exceção.
"""

class SenhaFracaError(Exception):
    def __init__(self):
        self.msg = "A senha é fraca. Deve ter pelo menos 8 caracteres e um número"

def verifica_senha(senha):
    if len(senha) < 8 or not any(c.isdigit()for c in senha):
        raise SenhaFracaError()
        
try:
    senha = input("Digite a senha que deseja verificar:" )
    verifica_senha(senha)
    print("Senha aceitável")
except SenhaFracaError as e:
    print("Erro: ", e.msg)