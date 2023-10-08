import matplotlib.pyplot as plt
import seaborn as sns

def print_likes(bandas):
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Likes'].sum() for banda in bandas]

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))  # Ajuste o tamanho conforme necessário

    # Barra horizontal
    plt.bar(nomes, likes_totais)

    # Adicionar rótulos e título
    plt.xlabel('Total de Likes')
    plt.ylabel('Bandas')
    plt.title('Total de Likes por Banda')

    # Mostrar o gráfico
    plt.show()

def print_views(bandas):
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Views'].sum() for banda in bandas]

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))  # Ajuste o tamanho conforme necessário

    # Barra horizontal
    plt.bar(nomes, likes_totais, color="green")

    # Adicionar rótulos e título
    plt.xlabel('Total de Views')
    plt.ylabel('Bandas')
    plt.title('Total de Views por Banda')

    # Mostrar o gráfico
    plt.show()

def print_instrumentalidade(bandas):
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Instrumentalness'].sum() for banda in bandas]

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))  # Ajuste o tamanho conforme necessário

    # Barra horizontal
    plt.bar(nomes, likes_totais, color='Orange')

    # Adicionar rótulos e título
    plt.xlabel('Total de Instrumentalidade')
    plt.ylabel('Bandas')
    plt.title('Total de Instrumentalidade por Banda')

    # Mostrar o gráfico
    plt.show()

def print_valencia(bandas):
    nomes = [banda[0] for banda in bandas]
    likes_totais = [banda[1]['Valence'].sum() for banda in bandas]

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))  # Ajuste o tamanho conforme necessário

    # Barra horizontal
    plt.bar(nomes, likes_totais, color="Purple")

    # Adicionar rótulos e título
    plt.xlabel('Total de Valência')
    plt.ylabel('Bandas')
    plt.title('Total de Valência por Banda')

    # Mostrar o gráfico
    plt.show()

def teste(bandas):
    for banda, dados in bandas:
        sns.lmplot(x='Likes', y='Views', data=dados, fit_reg=True, hue='Artist')
        plt.title(f'Relação entre Likes e Views para {banda}')
        plt.show()