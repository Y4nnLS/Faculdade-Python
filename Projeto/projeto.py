import pandas as pd
import graficos

# Leitura do arquivo CSV (fora do loop)
caminho = "C:/Programação/Python/Faculdade/Projeto/Spotify_Youtube.csv"
df = pd.read_csv(caminho, encoding="latin-1")
print(df.info())

bandas = []

while True:
    banda = input("Digite o nome da banda ou do artista (ou 'sair' para encerrar): ")
    
    if banda.lower() == "sair":
        break
    
    df_banda = df[df['Artist'] == banda]

    if not df_banda.empty:
        df_res = df_banda.groupby(["Artist", "Track", "Views", "Likes", "Instrumentalness"])["Valence"].sum().reset_index()
        print(df_res)
        bandas.append((banda, df_res))
    else:
        print(f"Banda ou artista '{banda}' não encontrado.")

# Comparar as bandas (fora do loop)
for banda, df_res in bandas:
    print(f"\nComparando dados para {banda}:")
    print(df_res)

# Criar gráficos aqui (fora do loop)

graficos.print_likes(bandas)
graficos.print_views(bandas)
graficos.print_instrumentalidade(bandas)
graficos.print_valencia(bandas)
