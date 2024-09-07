from src.service_web_scraping.estrategia.estrategia_g1 import ExtracaoNoticias
from bs4 import BeautifulSoup
# G1
en = ExtracaoNoticias(
    url='https://g1.globo.com/rss/g1/planeta-bizarro/')
dados = en.obter_dados()
itens = en.extrair_dados(site=dados)
for item in itens:
    soup_cleaned = BeautifulSoup(
        item.description.get_text(), 'html.parser')
    final_text = soup_cleaned.get_text()
    print('titulo:', item.title.text)
    print('GUID:', item.guid.text)
    print('TEXTO_LIMPO: ',  soup_cleaned.find('img').attrs['src'])
    print('TEXTO: ', soup_cleaned.text)

    print()
