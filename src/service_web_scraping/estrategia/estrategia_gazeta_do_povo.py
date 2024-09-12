from typing import Dict, Generator
from src.service_web_scraping.estrategia.estrategia import Estrategia
from bs4 import BeautifulSoup
from datetime import datetime


class EstrategiaGazetaPovo(Estrategia[BeautifulSoup]):
    def __init__(self, url: str) -> None:
        super().__init__(url=url)
        self.__id_site = 1
        self.__nome = 'Gazeta do Povo'
        self.__categoria = self._url.split('/')[-1].split('.')[0]

    def extrair_dados(self, site: BeautifulSoup) -> Generator[Dict[str, str], None, None]:
        itens = site.findAll('item')
        for item in itens:
            soup = BeautifulSoup(
                item.description.get_text(), 'html.parser')
            descricao = soup.get_text()
            data_publicacao = datetime.strptime(
                item.pubdate.text.strip(), "%a, %d %b %Y %H:%M:%S GMT")
            data_publicacao = data_publicacao.strftime("%d/%m/%Y %H:%M:%S")
            yield {
                'ID_SITE': self.__id_site,
                'NOME_SITE': self.__nome,
                'TITULO_NOTICIA': item.title.text.strip(),
                'URL_NOTICIA':  item.guid.text.strip(),
                'URL_IMG': item.url.text.strip(),
                'DESCRICAO': descricao,
                'DATA_PUBLICACAO': data_publicacao
            }
