import requests
import time
from bs4 import BeautifulSoup

url = "http://localhost:8080"
num_requests = 10

print(f"Disparando {num_requests} requisições para {url}...")
print("-" * 40)

for i in range(num_requests):
    try:
        response = requests.get(url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')
        message = soup.find('h1').text

        print(f"Requisição {i+1}: Resposta -> '{message}'")

    except requests.exceptions.RequestException as e:
        print(f"Requisição {i+1}: Falha ao conectar - {e}")

    time.sleep(0.5)

print("-" * 40)
print("Teste concluído!")