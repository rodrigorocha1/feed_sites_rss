from src.extracao_noticias import ExtracaoNoticias
from bs4 import BeautifulSoup

en = ExtracaoNoticias(
    url='https://www.gazetadopovo.com.br/feed/rss/mundo.xml')
dados = en.obter_dados()
itens = en.extrair_dados(site=dados)
for item in itens:
    soup_cleaned = BeautifulSoup(
        item.description.get_text(), 'html.parser')
    final_text = soup_cleaned.get_text()
    print(item.title.text)
    print(item.url.text)
    print(item.guid.text)
    print(final_text)
    print(item.pubdate.text)
    print()
