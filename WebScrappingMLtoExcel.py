from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

count = 1

pesquisa = input(str('Quais anúncios deseja buscar?: '))

url = (f"https://lista.mercadolivre.com.br/{pesquisa}")

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"}

site = requests.get(url, headers=headers)

soup = bs(site.content, 'html.parser')

produtos = soup.findAll("li", class_="ui-search-layout__item")

lista_de_produtos = []

for produto in produtos:
    # Encontrar produto
    link = produto.find('a', class_="ui-search-item__group__element ui-search-link__title-card ui-search-link").get("href")

    # Título do produto

    titulo = produto.find('h2', class_="ui-search-item__title").get_text().strip()

    # Preço do produto

    cents = produto.find('span', class_="andes-money-amount__cents andes-money-amount__cents--superscript-24")
    if cents != None:

        preco = produto.find('span', class_="andes-money-amount__fraction").get_text().strip() + ","\
        + produto.find('span', class_="andes-money-amount__cents andes-money-amount__cents--superscript-24").get_text().strip()

        print(f'Produto: ', count)
        print(f'titulo: {titulo}\nlink: {link}\npreco: {preco}')
        print('\n\n')

        lista_de_produtos.append([titulo, preco, link])
    else:
        preco = produto.find('span', class_="andes-money-amount__fraction").get_text().strip()

        print(f'Produto: ', count)
        print(f'titulo: {titulo}\nlink: {link}\npreco: {preco}')
        print('\n\n')

        lista_de_produtos.append([titulo, preco, link])
    count = count + 1

lista_de_produtos_df = pd.DataFrame(lista_de_produtos)
lista_de_produtos_df.columns = ['Título', 'Valor', 'link']
lista_de_produtos_df.to_excel(f'{pesquisa}.xlsx')
lista_string = [enumerate(lista_de_produtos)]

