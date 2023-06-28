
import os
import argparse

parser = argparse.ArgumentParser(description='Exibe uma lista de URLs.')
parser.add_argument('-l', '--lista', type=str, help='Arquivo contendo a lista de URLs.')
args = parser.parse_args()
urls = args.lista

payload_xss_1 = "?q=XSS&search=XSS&query=XSS&keywords=XSS&term=XSS&text=XSS&input=XSS&value=XSS&username=XSS&password=XSS&name=XSS&email=XSS&comment=XSS&message=XSS&body=XSS&title=XSS&subject=XSS&description=XSS&content=XSS&id=XSS&user=XSS&uid=XSS&pid=XSS&eid=XSS&cid=XSS&gid=XSS&aid=XSS&tid=XSS&wid=XSS&lid=XSS&mid=XSS&fid=XSS&did=XSS&oid=XSS&vid=XSS&sid=XSS&rid=XSS&file=XSS&msg=XSS"
payload_xss_2 = "?redirect=XSS&return=XSS&url=XSS&link=XSS&next=XSS&callback=XSS&referrer=XSS&referer=XSS&target=XSS&destination=XSS&returnurl=XSS&return_uri=XSS&return_path=XSS&returnto=XSS&return_to=XSS&page=XSS&view=XSS&section=XSS&module=XSS&component=XSS&task=XSS&action=XSS&option=XSS&format=XSS&tmpl=XSS&layout=XSS&lang=XSS&language=XSS&charset=XSS&stylesheet=XSS&script=XSS&js=XSS"
payload_xss_3 = "?category=XSS&filter=XSS&sort=XSS&order=XSS&limit=XSS&offset=XSS&page_size=XSS&search_term=XSS&query_string=XSS&search_query=XSS&search_param=XSS&search_filter=XSS&search_sort=XSS&search_order=XSS&search_limit=XSS&search_offset=XSS&search_page_size=XSS&field=XSS&column=XSS&row=XSS&value=XSS"
payload_xss_4 = "?filtro=XSS&campo=XSS&valor=XSS&consulta=XSS&busca=XSS&categoria=XSS&produto=XSS&quantidade=XSS&preco=XSS&promocao=XSS&desconto=XSS&carrinho=XSS&compra=XSS&pedido=XSS&endereco=XSS&cliente=XSS&usuario=XSS&sessao=XSS&token=XSS&chave=XSS&configuracao=XSS&ajuste=XSS&pagina=XSS&exibicao=XSS&filtro_pesquisa=XSS&ordem=XSS&grupo=XSS&marca=XSS&imagem=XSS&banner=XSS&slider=XSS&cor=XSS&tamanho=XSS&estilo=XSS&link_externo=XSS&compartilhar=XSS&feed=XSS&seguir=XSS&curtir=XSS&compartilhamento=XSS&evento=XSS&notificacao=XSS"
payload_xss_5 = "?filter_query=XSS&sort_by=XSS&sort_order=XSS&limit=XSS&offset=XSS&page_size=XSS&start_page=XSS&end_page=XSS&total_results=XSS&results_per_page=XSS&current_page=XSS&selected_page=XSS&active_tab=XSS&tab_id=XSS&tab_index=XSS&tab_name=XSS&view_mode=XSS&display_mode=XSS&mode=XSS&lang_id=XSS&lang_code=XSS&country_id=XSS&country_code=XSS&currency=XSS&timezone=XSS&date_format=XSS&time_format=XSS&api_key=XSS&api_token=XSS&auth_token=XSS&access_token=XSS&session_id=XSS&session_key=XSS&session_token=XSS&signature=XSS&nonce=XSS"

execucao_xss_1 = "cat "+urls+"| urlfusion '/"+payload_xss_1+"' |airixss -payload '\"XSS' | grep -Ev 'Not'"
execucao_xss_2 = "cat "+urls+"| urlfusion '/"+payload_xss_2+"' |airixss -payload '\"XSS' | grep -Ev 'Not'"
execucao_xss_3 = "cat "+urls+"| urlfusion '/"+payload_xss_3+"' |airixss -payload '\"XSS' | grep -Ev 'Not'"
execucao_xss_4 = "cat "+urls+"| urlfusion '/"+payload_xss_4+"' |airixss -payload '\"XSS' | grep -Ev 'Not'"
execucao_xss_5 = "cat "+urls+"| urlfusion '/"+payload_xss_5+"' |airixss -payload '\"XSS' | grep -Ev 'Not'"

os.system(execucao_xss_1)
os.system(execucao_xss_2)
os.system(execucao_xss_3)
os.system(execucao_xss_4)
os.system(execucao_xss_5)
