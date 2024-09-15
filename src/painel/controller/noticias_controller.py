from src.painel.model.noticias_model import NoticasModel


class NoticasControler:

    def __init__(self) -> None:
        self.model = NoticasModel()

    def obter_noticias(self, site: str):
        self.model.obter_todas_noticias(nome_site=site)
