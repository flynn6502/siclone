import os
import re
import urllib.parse
import requests
from bs4 import BeautifulSoup

# Configurações do alvo
TARGET_URL = "http://www.metodologiameet.com.br/"
OUTPUT_DIR = "metodologia_meet_clone"

# Diretórios locais
DIRS = {
    'css': os.path.join(OUTPUT_DIR, 'css'),
    'js': os.path.join(OUTPUT_DIR, 'js'),
    'images': os.path.join(OUTPUT_DIR, 'images')
}

# Criar estrutura de pastas locais
for path in DIRS.values():
    os.makedirs(path, exist_ok=True)

# Headers para simular navegação comum (evitar bloqueios)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def download_file(url, folder):
    """Baixa um arquivo da URL fornecida e o salva na pasta local informada."""
    try:
        # Resolver URLs relativas
        full_url = urllib.parse.urljoin(TARGET_URL, url)
        parsed_url = urllib.parse.urlparse(full_url)
        
        # Extrair nome do arquivo de forma limpa (sem query params como ?ver=1.0)
        filename = os.path.basename(parsed_url.path)
        if not filename or '.' not in filename:
            return None

        # Limpar query string do nome do arquivo salvo localmente
        clean_filename = re.sub(r'[\?\#].*$', '', filename)
        local_path = os.path.join(folder, clean_filename)

        # Fazer download do arquivo se ainda não existir
        if not os.path.exists(local_path):
            response = requests.get(full_url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                with open(local_path, 'wb') as f:
                    f.write(response.content)
                print(f"[+] Baixado: {clean_filename}")
            else:
                print(f"[-] Erro {response.status_code} ao baixar: {full_url}")
                return None
        return clean_filename
    except Exception as e:
        print(f"[!] Falha ao baixar {url}: {e}")
        return None

def main():
    print(f"[*] Acessando {TARGET_URL} ...")
    response = requests.get(TARGET_URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"[!] Não foi possível acessar o site. Status: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # 1. Extrair e reescrever CSS (<link rel="stylesheet">)
    print("\n[*] Baixando arquivos CSS...")
    for link in soup.find_all('link', rel=lambda x: x and 'stylesheet' in x.lower()):
        href = link.get('href')
        if href:
            saved_name = download_file(href, DIRS['css'])
            if saved_name:
                link['href'] = f"css/{saved_name}"

    # 2. Extrair e reescrever JavaScript (<script src="...">)
    print("\n[*] Baixando arquivos JS...")
    for script in soup.find_all('script', src=True):
        src = script.get('src')
        if src:
            saved_name = download_file(src, DIRS['js'])
            if saved_name:
                script['src'] = f"js/{saved_name}"

    # 3. Extrair e reescrever Imagens (<img>, <link icon>, etc)
    print("\n[*] Baixando Imagens...")
    for img in soup.find_all(['img', 'source']):
        src = img.get('src') or img.get('srcset')
        if src:
            # Pega a primeira URL em caso de srcset
            clean_src = src.split(',')[0].split(' ')[0]
            saved_name = download_file(clean_src, DIRS['images'])
            if saved_name:
                img['src'] = f"images/{saved_name}"
                if img.has_attr('srcset'):
                    del img['srcset']

    # 4. Salvar o arquivo index.html refatorado
    index_path = os.path.join(OUTPUT_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    print(f"\n[✓] Sucesso! Todo o conteúdo foi baixado e organizado na pasta '{OUTPUT_DIR}'.")
    print(f"    - Index: {index_path}")
    print(f"    - CSS: {DIRS['css']}")
    print(f"    - JS: {DIRS['js']}")
    print(f"    - Imagens: {DIRS['images']}")

if __name__ == "__main__":
    main()