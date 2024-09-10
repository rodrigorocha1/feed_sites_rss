from typing import Dict, Generator
from src.service_web_scraping.estrategia.estrategia import Estrategia
from bs4 import BeautifulSoup
from datetime import datetime


class EstrategiaNoticiasMinuto(Estrategia[BeautifulSoup]):
    def __init__(self, url: str) -> None:
        super().__init__(url=url)
        self.__id = 3
        self.__nome = 'Noticias Minuto'

    def extrair_dados(self, site: BeautifulSoup) -> Generator[Dict[str, str], None, None]:
        itens = site.findAll('item')
        for item in itens:
            data_hora_publicacao = datetime.strptime(
                item.pubdate.text.strip(), '%Y-%m-%d %H:%M:%S')
            data_hora_publicacao = data_hora_publicacao.strftime(
                '%d/%m/%Y %H:%M:%S')
            yield {
                'TITULO_NOTICIA': item.title.text.strip(),
                'URL_NOTICIA': item.guid.text.strip(),
                'URL_IMG': item.enclosure.attrs['url'],
                'DESCRICAO': item.description.text,
                'data_pubicacao': data_hora_publicacao
            }
