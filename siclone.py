import argparse
import os
import re
import urllib.parse

import requests
from bs4 import BeautifulSoup

DEFAULT_URL = "http://www.metodologiameet.com.br/"
DEFAULT_OUTPUT_DIR = "metodologia_meet_clone"

# Headers para simular navegação comum (evitar bloqueios)
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


def _download_file(url, folder, base_url, headers, timeout):
    """Baixa um arquivo (relativo a base_url) e o salva na pasta local informada."""
    try:
        full_url = urllib.parse.urljoin(base_url, url)
        parsed_url = urllib.parse.urlparse(full_url)

        # Extrair nome do arquivo de forma limpa (sem query params como ?ver=1.0)
        filename = os.path.basename(parsed_url.path)
        if not filename or '.' not in filename:
            return None

        clean_filename = re.sub(r'[\?\#].*$', '', filename)
        local_path = os.path.join(folder, clean_filename)

        if not os.path.exists(local_path):
            response = requests.get(full_url, headers=headers, timeout=timeout)
            if response.status_code != 200:
                print(f"[-] Erro {response.status_code} ao baixar: {full_url}")
                return None
            with open(local_path, 'wb') as f:
                f.write(response.content)
            print(f"[+] Baixado: {clean_filename}")
        return clean_filename
    except Exception as e:
        print(f"[!] Falha ao baixar {url}: {e}")
        return None


def clone_site(target_url, output_dir, headers=None, timeout=10):
    """
    Clona uma página estática: baixa HTML, CSS, JS e imagens, e reescreve
    os caminhos no HTML para apontarem para as pastas locais.

    Retorna um dict com os caminhos (index_path, css_dir, js_dir, images_dir)
    gerados dentro de output_dir.
    """
    headers = headers or DEFAULT_HEADERS
    dirs = {
        'css': os.path.join(output_dir, 'css'),
        'js': os.path.join(output_dir, 'js'),
        'images': os.path.join(output_dir, 'images'),
    }
    for path in dirs.values():
        os.makedirs(path, exist_ok=True)

    print(f"[*] Acessando {target_url} ...")
    response = requests.get(target_url, headers=headers, timeout=timeout)
    if response.status_code != 200:
        raise RuntimeError(f"Não foi possível acessar o site. Status: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    # 1. Extrair e reescrever CSS (<link rel="stylesheet">)
    print("\n[*] Baixando arquivos CSS...")
    for link in soup.find_all('link', rel=lambda x: x and 'stylesheet' in x.lower()):
        href = link.get('href')
        if href:
            saved_name = _download_file(href, dirs['css'], target_url, headers, timeout)
            if saved_name:
                link['href'] = f"css/{saved_name}"

    # 2. Extrair e reescrever JavaScript (<script src="...">)
    print("\n[*] Baixando arquivos JS...")
    for script in soup.find_all('script', src=True):
        src = script.get('src')
        if src:
            saved_name = _download_file(src, dirs['js'], target_url, headers, timeout)
            if saved_name:
                script['src'] = f"js/{saved_name}"

    # 3. Extrair e reescrever Imagens (<img>, <link icon>, etc)
    print("\n[*] Baixando Imagens...")
    for img in soup.find_all(['img', 'source']):
        src = img.get('src') or img.get('srcset')
        if src:
            # Pega a primeira URL em caso de srcset
            clean_src = src.split(',')[0].split(' ')[0]
            saved_name = _download_file(clean_src, dirs['images'], target_url, headers, timeout)
            if saved_name:
                img['src'] = f"images/{saved_name}"
                if img.has_attr('srcset'):
                    del img['srcset']

    # 4. Salvar o arquivo index.html refatorado
    index_path = os.path.join(output_dir, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    print(f"\n[✓] Sucesso! Todo o conteúdo foi baixado e organizado na pasta '{output_dir}'.")
    print(f"    - Index: {index_path}")
    print(f"    - CSS: {dirs['css']}")
    print(f"    - JS: {dirs['js']}")
    print(f"    - Imagens: {dirs['images']}")

    return {
        'index_path': index_path,
        'css_dir': dirs['css'],
        'js_dir': dirs['js'],
        'images_dir': dirs['images'],
    }


def main():
    parser = argparse.ArgumentParser(description="Clona uma página estática da web para uso offline.")
    parser.add_argument('url', nargs='?', default=DEFAULT_URL, help="URL do site a ser clonado.")
    parser.add_argument('output_dir', nargs='?', default=DEFAULT_OUTPUT_DIR, help="Pasta de saída para o clone.")
    args = parser.parse_args()
    clone_site(args.url, args.output_dir)


if __name__ == "__main__":
    main()
