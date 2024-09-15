from sqlalchemy import Column, Integer, String, ForeignKey
from src.painel.model.config_base import Base


class Noticias(Base):

    __tablename__ = "NOTICIA"

    ID_NOTICIA = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    ID_SITE = Column(Integer, ForeignKey('SITE.ID_SITE'), nullable=False)
    TITULO_NOTICIA = Column(String)
    URL_NOTICIA = Column(String)
    URL_IMG = Column(String)
    DESCRICAO = Column(String)
    DATA_PUBLICACAO = Column(String)
    CATEGORIA = Column(String)

    def __repr__(self):
        return (
            f"Noticias [\n"
            f"  ID_NOTICIA={self.ID_NOTICIA},\n"
            f"  ID_SITE={self.ID_SITE},\n"
            f"  TITULO_NOTICIA={self.TITULO_NOTICIA},\n"
            f"  URL_NOTICIA={self.URL_NOTICIA},\n"
            f"  URL_IMG={self.URL_IMG},\n"
            f"  DESCRICAO={self.DESCRICAO},\n"
            f"  DATA_PUBLICACAO={self.DATA_PUBLICACAO},\n"
            f"  CATEGORIA={self.CATEGORIA}\n"
            f"]"
        )
