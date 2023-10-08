"""
Crie uma função que realiza uma chamada de API para obter dados. Trate as exceções de conexão, timeout e outras possíveis falhas.
"""
import requests

def get_data_from_api(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)
        return None
    
get_data_from_api("https>//w3schools.com/python/demopage.htm")