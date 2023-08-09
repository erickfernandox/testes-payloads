import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def add_double_slash(url):
    # Verifica se a URL já possui duas barras após "https:"
    if url.startswith("https://") and not url.startswith("https:////"):
        parts = url.split("/")
        
        # Verifica se a URL possui uma suburl após o domínio
        if len(parts) > 3:
            # Insere uma segunda barra após o domínio
            parts[2] += "/"
            new_url = "/".join(parts)
            return new_url
        else:
            return url  # A URL não possui uma suburl após o domínio
    else:
        return url  # A URL não começa com "https:"

def check_double_slash_in_html(url):
    try:
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=3)  # Limite de redirecionamentos personalizado
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        response = session.get(url, verify=True)  # Habilita a verificação de certificado
        if response.status_code == 200:
            html_content = response.text
            parsed_url = urlparse(url)
            sub_url = parsed_url.netloc + parsed_url.path
            if '="//' + url.split('/')[3] in html_content:
                return True
    except requests.exceptions.SSLError:
        pass  # Lidar com o erro de SSL
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a double slash to URLs in a text file.")
    parser.add_argument("-l", "--list", required=True, help="Path to the input text file with URLs")
    args = parser.parse_args()

    with open(args.list, 'r') as file:
        urls = file.readlines()

    new_urls = [add_double_slash(url.strip()) for url in urls]

    for new_url in new_urls:
        print("Checking:", new_url)
        if check_double_slash_in_html(new_url):
            print("\033[32mDouble slash found in HTML!\033[0m")
        else:
            print("Double slash not found in HTML.")
