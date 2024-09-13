from typing import Generator, Dict
from datetime import datetime
from bs4 import BeautifulSoup
from src.service_web_scraping.estrategia.estrategia import Estrategia


class EstrategiaG1(Estrategia[BeautifulSoup]):

    def __init__(self, url: str) -> None:

        super().__init__(url=url)
        self.__id_site = 2
        self.__nome = 'G1'
        self.__categoria = self._url.split('/')[-2]

    def extrair_dados(self, site: BeautifulSoup) -> Generator[Dict[str, str], None, None]:
        """_summary_

        Args:
            site (BeautifulSoup): _description_

        Yields:
            Generator[Dict[str, str], None, None]: _description_
        """
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
                'ID_SITE': self.__id_site,
                'NOME_SITE': self.__nome,
                'TITULO_NOTICIA': noticia.title.text.strip(),
                'URL_NOTICIA':  noticia.guid.text.strip(),
                'URL_IMG': url_img.strip() if url_img is not None else None,
                'DESCRICAO': soup.text.strip().replace('\n', ' '),
                'CATEGORIA': self.__categoria,
                'DATA_PUBLICACAO': data_publicacao
            }
