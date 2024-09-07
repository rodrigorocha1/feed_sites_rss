from typing import Dict, Generator
from src.service_web_scraping.estrategia.estrategia import Estrategia
from bs4 import BeautifulSoup


class EstrategiaGazetaPovo(Estrategia[BeautifulSoup]):
    def __init__(self, url: str) -> None:
        super().__init__(url=url)

    def extrair_dados(self, site: BeautifulSoup) -> Generator[Dict[str, str], None, None]:
        return super().extrair_dados(site)
