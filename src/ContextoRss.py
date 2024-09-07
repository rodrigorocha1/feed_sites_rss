from src.service_web_scraping.i_rss_extracao_strategy import IRssExtracaoStrategy


class NoticiasRss:
    def __init__(self, estrategia_web_scraping: IRssExtracaoStrategy) -> None:
        self.__estrategia_web_scraping = estrategia_web_scraping

    def executar_processamento(self):
        site = self.__estrategia_web_scraping.obter_dados()
        dados = self.__estrategia_web_scraping.extrair_dados(site=site)
        for dado in dados:
            print(dado)
