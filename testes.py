# Dicionário global para armazenar os usuários cadastrados
banco_usuarios = {}

def cadastrar_usuario(*args):
    novo_usuario = {}
    
    # Preenche os campos obrigatórios
    for campo in args:
        valor = input(f"Digite o valor para '{campo}': ")
        novo_usuario[campo] = valor
    
    # Preenche os campos adicionais
    while True:
        campo_adicional = input("Digite o nome de um campo adicional (ou 'sair' para finalizar): ")
        if campo_adicional.lower() == 'sair':
            break
        valor_adicional = input(f"Digite o valor para '{campo_adicional}': ")
        novo_usuario[campo_adicional] = valor_adicional
    
    # Armazena o novo usuário no dicionário global
    banco_usuarios[novo_usuario['nome']] = novo_usuario
    
    return novo_usuario

while True:
    print("Cadastro de Usuário")
    campos_obrigatorios = input("Digite os campos obrigatórios separados por vírgula: ")
    campos_obrigatorios_list = campos_obrigatorios.split(',')
    novo_usuario = cadastrar_usuario(*campos_obrigatorios_list)
    print("Usuário cadastrado:", novo_usuario)
    
    continuar = input("Deseja cadastrar outro usuário? (sim/não): ")
    if continuar.lower() == 'não':
        break

print("Usuários cadastrados:", banco_usuarios)
