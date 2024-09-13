from typing import Dict, Generator
from datetime import datetime
from bs4 import BeautifulSoup
from src.service_web_scraping.estrategia.estrategia import Estrategia


class EstrategiaNoticiasMinuto(Estrategia[BeautifulSoup]):
    def __init__(self, url: str) -> None:
        super().__init__(url=url)
        self.__id = 3
        self.__nome = 'Noticias Minuto'
        self.__categoria = self._url.split('/')[-1]

    def extrair_dados(self, site: BeautifulSoup) -> Generator[Dict[str, str], None, None]:
        itens = site.findAll('item')
        for item in itens:
            data_hora_publicacao = datetime.strptime(
                item.pubdate.text.strip(), '%Y-%m-%d %H:%M:%S')
            data_hora_publicacao = data_hora_publicacao.strftime(
                '%d/%m/%Y %H:%M:%S')
            yield {
                'ID_SITE': self.__id,
                'NOME_SITE': self.__nome,
                'TITULO_NOTICIA': item.title.text.strip(),
                'URL_NOTICIA': item.guid.text.strip(),
                'URL_IMG': item.enclosure.attrs['url'],
                'DESCRICAO': item.description.text,
                'CATEGORIA': self.__categoria,
                'DATA_PUBLICACAO': data_hora_publicacao
            }
