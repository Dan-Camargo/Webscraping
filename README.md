# Webscraping

I'm going to leave some codes that i wrote for studying python automations and webscraping using Requests Pandas and Selenium

# Webscraping e Automação Web

Códigos de estudo para automação web e webscraping usando Python com Requests, Pandas, Selenium e BeautifulSoup.

## Tecnologias

- Python
- Selenium WebDriver
- BeautifulSoup4
- Requests
- Pandas
- WebDriver Manager

## Projetos

### SigaLogin.py
Automação de login no sistema SIGA (Centro Paula Souza)
- Login automatizado com credenciais do usuário
- Uso do Firefox WebDriver
- Navegação automática após login

### WebScrappingMLtoExcel.py
Extração de dados do Mercado Livre
- Busca produtos por termo específico
- Extrai título, preço e link dos anúncios
- Exporta resultados para planilha Excel
- Tratamento de diferentes formatos de preço

### WebScrappingSky
Extração de documentação técnica da Totvs
- Coleta URLs de páginas de API
- Extrai títulos e conteúdo de documentação
- Busca específica por seções "Objetivo" e "Chamada"
- Navegação automática entre páginas

## Habilidades Desenvolvidas

- Automação de navegadores web com Selenium
- Web scraping com BeautifulSoup e Requests
- Manipulação de dados HTML/XML
- Tratamento de headers HTTP e User-Agent
- Exportação de dados para Excel
- Localização de elementos por XPath e CSS selectors
- Gerenciamento automático de drivers

## Como Executar

```bash
pip install selenium beautifulsoup4 requests pandas webdriver-manager
```

Execute cada script individualmente:
```bash
python SigaLogin.py
python WebScrappingMLtoExcel.py
python WebScrappingSky
```

## Casos de Uso

- Automação de login em sistemas educacionais
- Monitoramento de preços em e-commerce
- Extração de documentação técnica
- Coleta automatizada de dados web
