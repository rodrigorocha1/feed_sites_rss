from src.service_web_scraping.estrategia.estrategia_gazeta_do_povo import EstrategiaGazetaPovo


if __name__ == '__main__':
    enm = EstrategiaGazetaPovo(
        url='https://www.noticiasaominuto.com.br/rss/tech'
    )

    site = enm.obter_dados()
    print(enm.nome, enm.id_site)
