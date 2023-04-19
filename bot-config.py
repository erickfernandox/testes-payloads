import os
import argparse

parser = argparse.ArgumentParser()

domain = "all_domain"

parser.add_argument("-l", "--lista", help="Caminho da Lista")
args = parser.parse_args()
path = args.lista

os.system("mkdir "+domain)

# Lê o arquivo e armazena cada linha em uma lista
with open(path, "r") as file:
    lista = file.readlines()

# Imprime cada elemento da lista em um loop
for url in lista:

    os.system("echo '"+url+"'|httpx > "+domain+"/subf-tmp.txt")

    os.system("cat "+domain+"/subf-tmp.txt | gauplus > "+domain+"/all_domain-gauplus_2.txt")

    os.system("cat "+domain+"/subf-tmp.txt |katana > "+domain+"/katana-tmp-2.txt") 

    #Executa o SlicePathsURL pra cortar os URLS
    os.system("cat "+domain+"/all_domain-gauplus_2.txt "+domain+"/katana-tmp-2.txt |slicepathsurl -l 3|grep -Ev '4|5|6|7|8|9|\)|\(|\?'|httpx > "+domain+"/urls_slice_2.txt")

    if url.startswith("https://"):
        url = url.replace("https://", "", 1)
    elif url.startswith("http://"):
        url = url.replace("http://", "", 1)

    #Open Redirect
    os.system("cat "+domain+"/urls_slice_2.txt | nuclei -t /root/nuclei-templates/exposures/configs/ -t /root/nuclei-templates/exposures/logs -c 75 > "+domain+"/configs_"+url)

    #Git e CRLF Injection
    #os.system("cat "+domain+"/urls_slice.txt | nuclei -tags git,crlf -c 75 > "+domain+"/git-crlf.txt_"+url)

    #Swagger XSS
    #os.system("cat "+domain+"/urls_slice.txt | nuclei -t  multiples-swagger-xss-indentify.yaml -c 75 > "+domain+"/swagger-xss_"+url)
