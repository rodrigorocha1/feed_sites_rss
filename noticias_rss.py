from src.service_web_scraping.estrategia.i_rss_extracao_strategy import IRssExtracaoStrategy
from src.service_web_scraping.estrategia.estrategia_g1 import EstrategiaG1
from src.infa_banco.iinfra_banco import IInfraBanco
from src.infa_banco.conexao_sqlite import ConexaoSqlite


class NoticiasRss:
    def __init__(self, estrategia_web_scraping: IRssExtracaoStrategy, banco_dados: IInfraBanco) -> None:
        self.__estrategia_web_scraping = estrategia_web_scraping
        self.__banco = banco_dados

    def executar_processamento(self):
        dados = self.__estrategia_web_scraping
        site = self.__estrategia_web_scraping.obter_dados()
        dados = self.__estrategia_web_scraping.extrair_dados(site=site)
        self.__banco.conectar_banco()
        for dado in dados:
            campos = tuple(dado.keys())
            valores = list(dado.values())
            dados_campos_sites = campos[0:2]
            dados_valores_sites = valores[0:2]

            print('*' * 20)
            dados_campos_noticias = (campos[0],) + campos[2:]
            valores_campos_noticias = [valores[0]] + valores[2:]
            print(valores_campos_noticias)

            break
        self.__banco.fechar_conexao()


if __name__ == '__main__':

    lista_estrategia = [
        EstrategiaG1(url='https://g1.globo.com/rss/g1/tecnologia/'),

    ]
    for estrategia in lista_estrategia:

        ns = NoticiasRss(
            estrategia_web_scraping=estrategia,
            banco_dados=ConexaoSqlite()
        )
        ns.estrategia = estrategia
        ns.executar_processamento()
