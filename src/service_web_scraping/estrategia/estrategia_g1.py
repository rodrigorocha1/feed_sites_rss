from src.service_web_scraping.estrategia.estrategia import Estrategia
import requests
from typing import Generator, Dict
from bs4 import BeautifulSoup
from datetime import datetime


class EstrategiaG1(Estrategia[BeautifulSoup]):

    def __init__(self, url: str) -> None:
        super().__init__(url=url)
        self.__id = 2
        self.__nome = 'G1'
        self.__categoria = self._url.split('/')[-2]

    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    def extrair_dados(self, site: BeautifulSoup) -> Generator[Dict[str, str], None, None]:
        itens = site.findAll('item')
        for noticia in itens:
            soup = BeautifulSoup(
                noticia.description.get_text(),
                'html.parser')
            img_tag = soup.find('img')
            url_img = img_tag.attrs['src'] if img_tag and 'src' in img_tag.attrs else None
            data_publicacao = datetime.strptime(
                noticia.pubdate.text.strip(), "%a, %d %b %Y %H:%M:%S %z")
            data_publicacao = data_publicacao.strftime("%d/%m/%Y %H:%M:%S")
            yield {

                'TITULO_NOTICIA': noticia.title.text.strip(),
                'URL_NOTICIA':  noticia.guid.text.strip(),
                'URL_IMG': url_img.strip() if url_img is not None else None,
                'DESCRICAO': soup.text.strip().replace('\n', ' '),
                'DATA_PUBLICACAO': data_publicacao
            }
