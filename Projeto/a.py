import pandas as pd
import graficos

def print_menu():
    print("+--------------MENU---------------+")
    print("| [1] Buscar uma banda            |")
    print("| [2] Comparar as bandas buscadas |")
    print("| [3] Mostrar estatísticas        |")
    print("| [4] Sair                        |")
    print("+---------------------------------+")

caminho = "C:/Programação/Python/Faculdade/Projeto/Spotify_Youtube.csv"
df = pd.read_csv(caminho, encoding="latin-1")
print(df.info())

bandas = []

while True:
    
    print_menu()
    try:
        op = int(input("Selecione uma das opções acima: "))
    except ValueError:
        continue

    match op:
        case 1:
            banda = input("Digite o nome da banda ou do artista (ou 'sair' para encerrar): ")
            
            df_banda = df[df['Artist'] == banda]
            if not df_banda.empty:
                df_res = df_banda.groupby(["Artist", "Track", "Views", "Likes", "Instrumentalness"])["Valence"].sum().reset_index()
                print(df_res)
                bandas.append((banda, df_res))
            else:
                print(f"Banda ou artista '{banda}' não encontrado.")
        case 2:
            for banda, df_res in bandas:
                print(f"\nComparando dados para {banda}:")
                print(df_res)
        case 3:
            graficos.print_likes(bandas)
            graficos.print_views(bandas)
            graficos.print_instrumentalidade(bandas)
            graficos.print_valencia(bandas)
            graficos.teste(bandas)
        case 4:
            break
        case _:
            print("Opção não encontrada...")

