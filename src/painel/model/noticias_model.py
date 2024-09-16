from src.painel.model.noticias import Noticias
from src.painel.model.site import Site
from src.painel.model.database_connection import DatabaseConnection
from typing import Tuple
import pandas as pd
from sqlalchemy import and_


class NoticasModel:
    def __init__(self) -> None:
        self.db = DatabaseConnection()
        self.db.iniciar_banco()

    def obter_sessao(self):
        return self.db.obter_sessao()

    def obter_todas_noticias(self, nome_site: str, categoria: str) -> pd.DataFrame:
        session = self.obter_sessao()

        try:
            noticias = session.query(Noticias) \
                .filter(
                    and_(
                        Site.NOME_SITE == nome_site,
                        Noticias.CATEGORIA == categoria
                    )
            )    \
                .join(Site, Noticias.ID_SITE == Site.ID_SITE) \
                .with_entities(
                    Site.NOME_SITE,
                    Noticias.CATEGORIA,
                    Noticias.TITULO_NOTICIA,
                    Noticias.DESCRICAO,
                    Noticias.URL_NOTICIA,
                    Noticias.URL_IMG
            ).all()
            df = pd.DataFrame(noticias, columns=[
                'NOME_SITE',
                'CATEGORIA',
                'TITULO_NOTICIA',
                'DESCRICAO',
                'URL_NOTICIA',
                'URL_IMG'
            ]).astype({
                'NOME_SITE': 'string',
                'CATEGORIA': 'string',
                'TITULO_NOTICIA': 'string',
                'DESCRICAO': 'string',
                'URL_NOTICIA': 'string',
                'URL_IMG': 'string'
            })

            return df

        finally:
            session.close()
