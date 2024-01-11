import requests
from bs4 import BeautifulSoup
from datetime import datetime

data_e_dia = datetime.now().strftime("%Y-%m-%d %A")
data_de_hoje = datetime.now().strftime('%Y-%m-%d')

headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}

def extrair_noticias_g1(url):
    print(f"Data e dia da execução: {data_e_dia}")

    resposta = requests.get(url, headers=headers)
    
    if resposta.status_code == 200:
        site = BeautifulSoup(resposta.text, 'html.parser')

        noticia = site.find_all('div', class_="feed-post-body")
        print("--------------------------------------------")
        for noticias in noticia:
            titulo = noticias.find('a', class_="feed-post-link")
            print(titulo.text)
            subtitulo = noticias.find('div', class_="feed-post-body-resumo")
            if subtitulo != None:
                print(subtitulo.text)
            print("--------------------------------------------")
    else:
        print(f"Erro ao obter a página. Código de status: {resposta.status_code}")

def extrair_noticias_bbc(url):
    print(f"Data e dia da execução: {data_e_dia}")

    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 200:
        site = BeautifulSoup(resposta.text, 'html.parser')

        noticias =  site.find_all('div', class_="gs-c-promo-body")
        print("--------------------------------------------")
        for noticia in noticias:
            titulo = noticia.find('h3', class_='gs-c-promo-heading__title')
            subtitulo = noticia.find('p', class_="gs-c-promo-summary")
            print(titulo.text)
            if subtitulo != None:
                print(subtitulo.text)
            print("--------------------------------------------")
    else:
        print(f"Erro ao obter a página. Código de status: {resposta.status_code}")

def extrair_noticias_bbc_portuguese(url):
    print(f"Data e dia da execução: {data_e_dia}")

    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 200:
        site = BeautifulSoup(resposta.text, 'html.parser')
        
        noticias_hoje = site.find_all('div', class_='promo-text')
        
        for noticia in noticias_hoje:
            data_noticia = noticia.find('time', class_="promo-timestamp")['datetime']
            if data_noticia.lower() == data_de_hoje.lower():
                titulo = noticia.find('h2').text
                print(f"Título da Notícia: {titulo}")
    else:
        print(f"Erro ao obter a página. Código de status: {resposta.status_code}")

url_g1 = 'https://g1.globo.com/'
url_bbc_news_portuguese = 'https://www.bbc.com/portuguese/topics/c404v027pd4t'
url_bbc_news = 'https://www.bbc.com/news'

#extrair_noticias_bbc(url_bbc_news)
#extrair_noticias_g1(url_g1)
#extrair_noticias_bbc_portuguese(url_bbc_news_portuguese)

