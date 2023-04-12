import os

domain = input("Digita o Domain: ")

os.system("mkdir "+domain)

os.system("subfinder -d  "+domain+" | httpx > "+domain+"/subf-tmp.txt")

os.system("cat "+domain+"/subf-tmp.txt | gauplus > "+domain+"/all_domain-gauplus.txt")

os.system("cat "+domain+"/subf-tmp.txt |katana > "+domain+"/katana-tmp.txt") 

#Executa o SlicePathsURL pra cortar os URLS
os.system("cat "+domain+"/all_domain-gauplus.txt "+domain+"/katana-tmp.txt | grep -Ev ':80|embed'|slicepathsurl |grep -Ev '4|5|6|7|8|9' > "+domain+"/urls_slice.txt")

#Open Redirect
os.system("cat "+domain+"/urls_slice.txt | nuclei -t /root/nuclei-templates/cves/2022/CVE-2022-28923.yaml -t /root/nuclei-templates/vulnerabilities/generic/open-redirect.yaml -c 75 > "+domain+"/openredirect.txt")

#Git e CRLF Injection
os.system("cat "+domain+"/urls_slice.txt | nuclei -tags git,crlf -c 75 > "+domain+"/git-crlf.txt")

#Swagger XSS
os.system("cat "+domain+"/urls_slice.txt | nuclei -t  multiples-swagger-xss-indentify.yaml -c 75 > "+domain+"/swagger-xss.txt")

#Pasta Exposta
os.system("cat "+domain+"/urls_slice.txt | httpx -title | grep 'Index of' > "+domain+"/indexof.txt")

#Path Traversal
os.system("cat "+domain+"/urls_slice.txt | nuclei -tags traversal -c 75 > "+domain+"/traversal.txt")

#Informações Expostas
os.system("cat "+domain+"/urls_slice.txt | nuclei -t /root/nuclei-templates/exposures/configs/ -t /root/nuclei-templates/exposures/logs/  -t /root/nuclei-templates/exposures/apis/ -t /root/nuclei-templates/exposures/backups/ -c 75 > "+domain+"/exposures.txt")

#Ultimos CVES 2022 e 2023
os.system("cat "+domain+"/urls_slice.txt | nuclei -t /root/nuclei-templates/cves/2022/ -t /root/nuclei-templates/cves/2023/ -c 75 > "+domain+"/ultimos-cves.txt")
