
import os
import argparse

parser = argparse.ArgumentParser(description='Exibe uma lista de URLs.')
parser.add_argument('-l', '--lista', type=str, help='Arquivo contendo a lista de URLs.')
args = parser.parse_args()
urls = args.lista

payload_xss_1 = "?q=XSS&search=XSS&query=XSS&keywords=XSS&term=XSS&text=XSS&input=XSS&value=XSS&username=XSS&password=XSS&name=XSS&email=XSS&comment=XSS&message=XSS&body=XSS&title=XSS&subject=XSS&description=XSS&content=XSS&id=XSS&user=XSS&uid=XSS&pid=XSS&eid=XSS&cid=XSS&gid=XSS&aid=XSS&tid=XSS&wid=XSS&lid=XSS&mid=XSS&fid=XSS&did=XSS&oid=XSS&vid=XSS&sid=XSS&rid=XSS&file=XSS&msg=XSS"
payload_xss_2 = "?redirect=XSS&return=XSS&url=XSS&link=XSS&next=XSS&callback=XSS&referrer=XSS&referer=XSS&target=XSS&destination=XSS&returnurl=XSS&return_uri=XSS&return_path=XSS&returnto=XSS&return_to=XSS&page=XSS&view=XSS&section=XSS&module=XSS&component=XSS&task=XSS&action=XSS&option=XSS&format=XSS&tmpl=XSS&layout=XSS&lang=XSS&language=XSS&charset=XSS&stylesheet=XSS&script=XSS&js=XSS"

execucao_xss_1 = "cat "+urls+"| urlfusion '/"+payload_xss_1+"' |airixss -payload '\"XSS' | grep -Ev 'Not'"
execucao_xss_2 = "cat "+urls+"| urlfusion '/"+payload_xss_2+"' |airixss -payload '\"XSS' | grep -Ev 'Not'"

os.system(execucao_xss_1)
os.system(execucao_xss_2)
