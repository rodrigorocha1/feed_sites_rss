from src.service_web_scraping.estrategia.i_rss_extracao_strategy import IRssExtracaoStrategy
from abc import abstractmethod
from typing import Dict, Generator, TypeVar, Generic
import requests
from bs4 import BeautifulSoup
from datetime import datetime


T1 = TypeVar('T1')


class Estrategia(IRssExtracaoStrategy[T1]):

    def __init__(self, url: str) -> None:
        self._url = url

    def obter_dados(self) -> BeautifulSoup:
        response = requests.get(self._url)
        html = response.text
        site = BeautifulSoup(html, 'html.parser')

        return site

    @abstractmethod
    def extrair_dados(self, site: T1) -> Generator[Dict[str, str], None, None]:
        pass
