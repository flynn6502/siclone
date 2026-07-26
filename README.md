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
