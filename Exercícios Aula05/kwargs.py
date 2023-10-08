def cadastra_pessoas(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for chave in kwargs:
        print(type(chave))
        print(f"chave -> {kwargs[chave]}")

cadastra_pessoas(alexandre=20, juliana=14)