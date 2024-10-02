# Frontend Testing Project (front-testing-py)

Este projeto contém testes automatizados de frontend para componentes como checkbox, drag and drop, dropdown, upload de arquivo, login e redirecionamento, utilizando Behave como framework BDD e Selenium WebDriver para automação do navegador.

## Requisitos

- Python 3.x
- Google Chrome
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatível com a versão do seu Chrome


### Passos para instalação

1. Clone o repositório:

   ```bash
   git clone https://seu-repositorio-url/front-testing-py.git
   cd front-testing-py
   
2. Instalando
   Crie um ambiente virtual para o Python:
        python -m venv venv
        source venv/bin/activate 
   Adicione o chromedrive o diretorio do $PATH 
   pip install -r requirements.txt

3. Executando

    behave
    ou
    behave features/nome_feature.feature


