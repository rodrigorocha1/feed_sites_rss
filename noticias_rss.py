from src.service_web_scraping.estrategia.i_rss_extracao_strategy import IRssExtracaoStrategy
from src.service_web_scraping.estrategia.estrategia_g1 import EstrategiaG1
from typing import List


class NoticiasRss:
    def __init__(self, estrategia_web_scraping: IRssExtracaoStrategy) -> None:
        self.__estrategia_web_scraping = estrategia_web_scraping

    def executar_processamento(self):
        site = self.__estrategia_web_scraping.obter_dados()
        dados = self.__estrategia_web_scraping.extrair_dados(site=site)
        for dado in dados:
            print(dado)
            print()


if __name__ == '__main__':
    url = 'https://g1.globo.com/rss/g1/tecnologia/'
    print(url.split('/'))

    # lista_estrategia = [
    #     EstrategiaG1(url='https://g1.globo.com/rss/g1/tecnologia/'),

    # ]
    # for estrategia in lista_estrategia:

    #     ns = NoticiasRss(estrategia_web_scraping=estrategia)
    #     ns.estrategia = estrategia
    #     ns.executar_processamento()
