import os
import argparse

parser = argparse.ArgumentParser(description='Exibe uma lista de URLs.')
parser.add_argument('-l', '--lista', type=str, help='Arquivo contendo a lista de URLs.')

# Parse dos argumentos
args = parser.parse_args()

payload_op_1 = "?redirect=https://example.com&url=https://example.com&link=https://example.com&return=https://example.com&next=https://example.com&return_url=https://example.com&return_uri=https://example.com&return_path=https://example.com&returnto=https://example.com&return_to=https://example.com&target=https://example.com&destination=https://example.com&returnPath=https://example.com&redirect_uri=https://example.com&redirect_url=https://example.com&goto=https://example.com"
payload_op_2 = "?continue=https://example.com&?next_url=https://example.com&dest=https://example.com&uri=https://example.com&go=https://example.com&to=https://example.com&returnuri=https://example.com&returnpath=https://example.com&return-path=https://example.com&callback=https://example.com&ref=https://example.com&path=https://example.com&page=https://example.com&view=https://example.com&redir=https://example.com&redirect_to=https://example.com&destination_url=https://example.com"

execucao_op_1 = "cat "+args.lista+"|httpx -path '/"+payload_op_1+"'-silent -fr -title|grep 'Example Domain'"
execucao_op_2 = "cat "+args.lista+"|httpx -path '/"+payload_op_2+"'-silent -fr -title|grep 'Example Domain'"

os.system(execucao_op_1)
os.system(execucao_op_2)

execucao_op_1 = "cat "+args.lista+"|httpx -path '/"+payload_op_1+"' -mr 'Location: https://example.com'"
execucao_op_2 = "cat "+args.lista+"|httpx -path '/"+payload_op_2+"' -mr 'Location: https://example.com'"

os.system(execucao_op_1)
os.system(execucao_op_2)
