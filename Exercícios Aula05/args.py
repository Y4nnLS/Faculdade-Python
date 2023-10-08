def faz_feira(dia, *frutas):
    print(f"{dia} comprei: ")
    for fruta in frutas:
        print(fruta, end=" ")
    print("")

faz_feira("Segunda", "maça", "banana")
faz_feira("Terça", "melancia")