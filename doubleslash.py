import argparse

def add_double_slash(url):
    # Verifica se a URL já possui duas barras após "https:"
    if url.startswith("https://") and not url.startswith("https:////"):
        parts = url.split("/")
        
        # Verifica se a URL possui uma suburl após o domínio
        if len(parts) > 3:
            # Insere uma segunda barra após o domínio
            parts[2] += "/"
            new_url = "/".join(parts)
            return new_url
        else:
            return url  # A URL não possui uma suburl após o domínio
    else:
        return url  # A URL não começa com "https://"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a double slash to URLs in a text file.")
    parser.add_argument("-l", "--list", required=True, help="Path to the input text file with URLs")
    args = parser.parse_args()

    with open(args.list, 'r') as file:
        urls = file.readlines()

    new_urls = [add_double_slash(url.strip()) for url in urls]

    for new_url in new_urls:
        print(new_url)
