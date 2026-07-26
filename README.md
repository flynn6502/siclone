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

1. Abra o arquivo `siclone.py` no seu editor de código (como o Cursor ou VS Code).
2. Edite a variável `TARGET_URL` com o endereço do site que deseja clonar:
```python
TARGET_URL = "[https://exemplo.com.br/](https://exemplo.com.br/)"
OUTPUT_DIR = "site_clonado"

```


3. Execute o script no terminal:
```bash
python siclone.py

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

## ⚠️ Isenção de Responsabilidade (Disclaimer)

Esta ferramenta foi desenvolvida estritamente para **fins educacionais, migração de projetos próprios e engenharia reversa autorizada**. O uso deste script para clonar sites sem a autorização prévia dos proprietários é de inteira responsabilidade do usuário. Respeite os direitos autorais e os termos de serviço das plataformas.

---

## 📄 Licença

Este projeto está sob a licença [MIT](https://www.google.com/search?q=LICENSE).

```

```
