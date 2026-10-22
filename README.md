# 🌀 Siclone.py

**Siclone.py** é um script em Python para clonar páginas estáticas da web e mapear seus recursos locais. Ele realiza o download do HTML, mapeia e baixa as dependências (estilos CSS, scripts JavaScript e imagens) e reescreve os caminhos no arquivo `index.html` para que o projeto funcione perfeitamente de forma offline.

---

## 🚀 Funcionalidades

- 📄 **Download do HTML:** Obtém a página fonte e formata o código para leitura limpa.
- 🎨 **Mapeamento de CSS:** Localiza e baixa todas as folhas de estilo (`<link rel="stylesheet">`).
- ⚡ **Mapeamento de JavaScript:** Baixa todos os scripts externos (`<script src="...">`).
- 🖼️ **Captura de Mídias:** Extrai imagens e vetores (`<img>`, `<source>`, favicon) e trata atributos complexos como `srcset`.
- 🔄 **Reescrita de Caminhos:** Atualiza as referências do HTML para apontar automaticamente para as pastas locais (`/css`, `/js`, `/images`).

---

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter o **Python 3.8+** instalado em sua máquina.

Você precisará das seguintes bibliotecas:
- [`requests`](https://pypi.org/project/requests/) — Para requisições HTTP.
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) — Para parsing e manipulação do HTML.

Instale as dependências executando:

```bash
pip install requests beautifulsoup4

```

---

## 📦 Instalação

1. Clone este repositório para sua máquina local:
```bash
git clone [https://github.com/seu-usuario/siclone.git](https://github.com/seu-usuario/siclone.git)
cd siclone

```


2. Certifique-se de que o arquivo `siclone.py` está no seu diretório de trabalho.

---

## ⚙️ Como Usar

Execute o script passando a URL e (opcionalmente) a pasta de saída:

```bash
python siclone.py https://exemplo.com.br/ site_clonado
```

Se nenhum argumento for informado, ele usa os valores padrão definidos em `DEFAULT_URL` e `DEFAULT_OUTPUT_DIR` no topo de `siclone.py`.

Você também pode chamar a função `clone_site(url, output_dir)` diretamente a partir de outro script Python:

```python
from siclone import clone_site

resultado = clone_site("https://exemplo.com.br/", "site_clonado")
print(resultado)  # {'index_path': ..., 'css_dir': ..., 'js_dir': ..., 'images_dir': ...}
```



---

## 📂 Estrutura Gerada

Após a execução, o **Siclone.py** criará uma pasta com a seguinte estrutura pronta para uso e refatoração:

```text
site_clonado/
├── index.html          # HTML refatorado apontando para os caminhos locais
├── css/                # Folhas de estilo (.css)
├── js/                 # Scripts (.js)
└── images/             # Imagens e ícones (.png, .jpg, .svg, .webp)

```

---

## 🤖 Servidor MCP

O projeto inclui um servidor [MCP](https://modelcontextprotocol.io/) (`mcp_server.py`) que expõe `clone_site()` como uma ferramenta (`clone_website`), permitindo que um agente de IA compatível (Claude Code, Claude Desktop, etc.) clone sites diretamente, sem precisar editar ou rodar o script manualmente.

1. Instale as dependências (inclui o pacote `mcp`):
```bash
pip install -r requirements.txt
```

2. Registre o servidor no seu cliente MCP. Exemplo de configuração (Claude Desktop/Code, `mcp.json`):
```json
{
  "mcpServers": {
    "siclone": {
      "command": "python",
      "args": ["/caminho/completo/para/mcp_server.py"]
    }
  }
}
```

3. Uma vez conectado, o agente terá acesso à ferramenta `clone_website(url, output_dir)`, que retorna os caminhos gerados (`index_path`, `css_dir`, `js_dir`, `images_dir`).

---

## ⚠️ Isenção de Responsabilidade (Disclaimer)

Esta ferramenta foi desenvolvida estritamente para **fins educacionais, migração de projetos próprios e engenharia reversa autorizada**. O uso deste script para clonar sites sem a autorização prévia dos proprietários é de inteira responsabilidade do usuário. Respeite os direitos autorais e os termos de serviço das plataformas.

---

## 📄 Licença

Este projeto está sob a licença [MIT](https://www.google.com/search?q=LICENSE).

```

```
