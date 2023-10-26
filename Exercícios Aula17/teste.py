import requests

url = 'http://127.0.0.1:5000/contatos/2'

response = requests.get(url)

with open('contato.json', 'r') as json_file:
    headers = { 'Content-Type' : 'application/json' }
    response = requests.post(url, data=json_file, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro', response.status_code)