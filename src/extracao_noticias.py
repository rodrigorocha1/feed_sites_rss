from src.service_web_scraping.iextracao import IExtracao
import requests
from bs4.element import ResultSet
from bs4 import BeautifulSoup


class ExtracaoNoticias(IExtracao[BeautifulSoup, ResultSet]):
    def __init__(self, url: str) -> None:
        self.__url = url

    def obter_dados(self) -> BeautifulSoup:
        response = requests.get(url=self.__url)
        html = response.text
        site = BeautifulSoup(html, 'html.parser')
        return site

    def extrair_dados(self, site: BeautifulSoup) -> ResultSet:
        itens = site.findAll('item')
        return itens
