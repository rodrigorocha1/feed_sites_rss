from src.painel.model.noticias import Noticias
from src.painel.model.site import Site
from src.painel.model.database_connection import DatabaseConnection
from typing import List


class NoticasModel:
    def __init__(self) -> None:
        self.db = DatabaseConnection()
        self.db.iniciar_banco()

    def obter_sessao(self):
        return self.db.obter_sessao()

    def obter_todas_noticias(self) -> List[Noticias]:
        session = self.obter_sessao()
        try:
            noticias = session.query(Noticias).all()
            return noticias
        finally:
            session.close()
