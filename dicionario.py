capitals = {
    'USA':'Washington DC',
    'India':'New Dehli',
    'China':'Beijing',
    'Russia':'Moscow'
}
teste = {
    1:1,
    2:2
}
capitals.update({'Brazil':'Brasilia'})
for key, value, in capitals.items():
    print(key, value)
capitals.update(teste)
print(teste)
for key, value, in capitals.items():
    print(key, value)