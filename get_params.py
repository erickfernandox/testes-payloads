import requests
from bs4 import BeautifulSoup

import argparse

# Criação do parser de argumentos
parser = argparse.ArgumentParser(description='Exibe uma lista de URLs.')
parser.add_argument('-l', '--lista', type=str, help='Arquivo contendo a lista de URLs.')

# Parse dos argumentos
args = parser.parse_args()

def get_input_values(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    input_tags = soup.find_all('input')

    values = []
    
    for tag in input_tags:
        name = tag.get('name')
        if name:
            values.append(f"{name}=XSS")

    return "&".join(values)

with open(args.lista, 'r') as f:
    # Loop através das linhas do arquivo
    for line in f:
        # Remove os espaços em branco e caracteres de nova linha
        url = line.strip()
        result = get_input_values(url)
        print(f"{url}?{result}")
