from src.service_web_scraping.estrategia.i_rss_extracao_strategy import IRssExtracaoStrategy
from src.service_web_scraping.estrategia.estrategia_g1 import EstrategiaG1
from src.service_web_scraping.estrategia.estrategia_gazeta_do_povo import EstrategiaGazetaPovo
from src.service_web_scraping.estrategia.estrategia_noticas_minuto import EstrategiaNoticiasMinuto
from src.infa_banco.iinfra_banco import IInfraBanco
from src.infa_banco.conexao_sqlite import ConexaoSqlite
from src.pacote_log.config_log import logger


class NoticiasRss:
    def __init__(self, estrategia_web_scraping: IRssExtracaoStrategy, banco_dados: IInfraBanco) -> None:
        self.__estrategia_web_scraping = estrategia_web_scraping
        self.__banco = banco_dados

    def executar_processamento(self):
        try:
            dados = self.__estrategia_web_scraping
            site = self.__estrategia_web_scraping.obter_dados()
            logger.info(f'Extraindo site: {site.title.text}')
            dados = self.__estrategia_web_scraping.extrair_dados(site=site)
            self.__banco.conectar_banco()
            for dado in dados:

                campos = tuple(dado.keys())
                valores = list(dado.values())
                dados_campos_sites = campos[0:2]
                dados_valores_sites = valores[0:2]

                dados_campos_noticias = (campos[0],) + campos[2:]
                valores_campos_noticias = [valores[0]] + valores[2:]
                self.__banco.inserir_dados(
                    tabela='SITE',
                    colunas=dados_campos_sites,
                    valores=dados_valores_sites
                )
                self.__banco.inserir_dados(
                    tabela='NOTICIA',
                    colunas=dados_campos_noticias,
                    valores=valores_campos_noticias
                )

            self.__banco.fechar_conexao()
        except ValueError as msg:
            logger.info(f'Erro de valor: {msg} site: {site.title.text}')


if __name__ == '__main__':

    lista_estrategia = [
        EstrategiaG1(
            url='https://g1.globo.com/rss/g1/tecnologia/'
        ),
        EstrategiaG1(
            url='https://g1.globo.com/rss/g1/turismo-e-viagem/'
        ),
        EstrategiaG1(
            url='https://g1.globo.com/rss/g1/planeta-bizarro/'
        ),
        EstrategiaG1(
            url='https://g1.globo.com/rss/g1/pa/para/'
        ),
        EstrategiaG1(
            url='https://g1.globo.com/rss/g1/sp/ribeirao-preto-franca/'
        ),
        EstrategiaGazetaPovo(
            url='https://www.gazetadopovo.com.br/feed/rss/mundo.xml'
        ),
        EstrategiaNoticiasMinuto(
            url='https://www.noticiasaominuto.com.br/rss/ultima-hora'
        ),
        EstrategiaNoticiasMinuto(
            url='https://www.noticiasaominuto.com.br/rss/tech'
        )

    ]
    for estrategia in lista_estrategia:

        ns = NoticiasRss(
            estrategia_web_scraping=estrategia,
            banco_dados=ConexaoSqlite()
        )
        ns.estrategia = estrategia
        ns.executar_processamento()
