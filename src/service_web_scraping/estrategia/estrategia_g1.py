from src.service_web_scraping.i_rss_extracao_strategy import IRssExtracaoStrategy
import requests
from typing import Generator, Dict
from bs4 import BeautifulSoup
from datetime import datetime


class EstrategiaG1(IRssExtracaoStrategy[BeautifulSoup]):

    def __init__(self, url: str) -> None:
        self.__url = url

    def obter_dados(self) -> BeautifulSoup:
        response = requests.get(self.__url)
        html = response.text
        site = BeautifulSoup(html, 'html.parser')

        return site

    def extrair_dados(self, site: BeautifulSoup) -> Generator[Dict[str, str], None, None]:
        itens = site.findAll('item')
        for noticia in itens:
            soup_cleaned = BeautifulSoup(
                noticia.description.get_text(),
                'html.parser')
            yield {
                'TITULO_NOTICIA': noticia.title.text,
                'URL_NOTICIA':  noticia.guid.text,
                'URL_IMG': soup_cleaned.find('img').attrs['src'],
                'DESCRICAO': soup_cleaned.text,
                'data_pubicacao': datetime.strptime(noticia.pubdate.text, "%a, %d %b %Y %H:%M:%S %Z").strftime("%d/%m/%Y")
            }
