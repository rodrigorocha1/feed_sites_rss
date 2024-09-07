from src.service_web_scraping.i_rss_extracao_strategy import IRssExtracaoStrategy
from bs4 import BeautifulSoup


class EstrategiaGazetaPovo(IRssExtracaoStrategy[BeautifulSoup]):
    def __init__(self, url: str) -> None:
        super().__init__()
