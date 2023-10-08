import pandas as pd

df = pd.read_csv("C:\Programação\Python\Faculdade\\votacao_10000linhas.csv", encoding="latin-1")

print(df.info())


df_sen = df[df['DS_CARGO'] == 'SENADOR']
print(df_sen.info())

df_res = df_sen.groupby(["NM_MUNICIPIO", "NM_VOTAVEL"])["QT_VOTOS"].sum().reset_index()
print(df_res)





df_result = df_sen.sort_values(by=["NM_MUNICIPIO", "QT_VOTOS"], ascending=([False, True]))
"""
for ind, linha in df_result.iterrows():
    print(f"{linha['NM_MUNICIPIO']} : {linha['NM_VOTAVEL']} ---> {linha['QT_VOTOS']}")
"""