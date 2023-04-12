import os

domain = input("Digita o Domain: ")

os.system("mkdir "+domain)

os.system("subfinder -d  "+domain+" | httpx > "+domain+"/subf-tmp.txt")

os.system("cat "+domain+"/subf-tmp.txt | gauplus > "+domain+"/all_domain-gauplus.txt")
#os.system("echo '"+domain+"'| httpx|katana > "+domain+"/katana-tmp.txt")
os.system("echo "+domain+"| katana > "+domain+"/katana-tmp.txt") 

os.system("cat "+domain+"/all_domain-gauplus.txt "+domain+"/katana-tmp.txt | grep -Ev ':80|embed|4|5|6|7|8|9'|slicepathsurl > "+domain+"/urls_slice.txt")

os.system("cat "+domain+"/urls_slice.txt | nuclei -t /root/nuclei-templates/cves/2022/CVE-2022-28923.yaml -t /root/nuclei-templates/vulnerabilities/generic/open-redirect.yaml > openredirect.txt")

os.system("cat "+domain+"/urls_slice.txt | nuclei -tags git,crlf > git-crlf.txt")

os.system("cat "+domain+"/urls_slice.txt | nuclei -t  multiples-swagger-xss-indentify.yaml > swagger-xss.txt")

os.system("cat "+domain+"/urls_slice.txt | httpx -title | grep 'Index of' > indexof.txt")

os.system("cat "+domain+"/urls_slice.txt | nuclei -tags traversal > traversal.txt")

os.system("cat "+domain+"/urls_slice.txt | nuclei -tags traversal > traversal.txt")
