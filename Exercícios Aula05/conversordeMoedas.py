def converter_cambio(qtde, moeda, **dicio):
    for chave in dicio:
        print(f"{qtde} em {moeda} = {qtde/dicio[chave]:.2f} em {chave}")

converter_cambio(100, "real", dolar=4.8, euro=5.7, peso=0.04,libra=7, ficticio=1)