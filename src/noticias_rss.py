from src.service_web_scraping.estrategia.i_rss_extracao_strategy import IRssExtracaoStrategy
from src.service_web_scraping.estrategia.estrategia_g1 import EstrategiaG1


class NoticiasRss:
    def __init__(self, estrategia_web_scraping: IRssExtracaoStrategy) -> None:
        self.__estrategia_web_scraping = estrategia_web_scraping

    @property
    def estrategria(self):
        return self.__estrategia_web_scraping

    @estrategria.setter
    def estrategia(self, estrategria: IRssExtracaoStrategy):
        self.__estrategia_web_scraping = estrategria

    def executar_processamento(self):
        site = self.__estrategia_web_scraping.obter_dados()
        dados = self.__estrategia_web_scraping.extrair_dados(site=site)
        for dado in dados:
            print(dado)


ns = NoticiasRss(estrategia_web_scraping=EstrategiaG1())

ns.executar_processamento()
