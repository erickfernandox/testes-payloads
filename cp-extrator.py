import argparse

# Função para extrair o valor de loadComponent de uma URL
def extract_component(url):
    start_pos = url.find("loadComponent=") + len("loadComponent=")
    end_pos = url.find("&", start_pos)
    if end_pos == -1:
        return url[start_pos:]
    else:
        return url[start_pos:end_pos]

# Lê o arquivo de entrada e extrai os valores de loadComponent
def extract_components_from_file(input_file):
    components = set()
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if "loadComponent=" in line:
                component = extract_component(line)
                components.add(component)
    return components

# Programa principal
if __name__ == "__main__":
    # Define os argumentos da linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--input_file", help="Arquivo de entrada contendo URLs")
    args = parser.parse_args()

    # Extrai os componentes dos URLs do arquivo de entrada
    components = extract_components_from_file(args.input_file)

    # Exibe os componentes na tela
    print("Componentes encontrados:")
    for component in components:
        print(component)
