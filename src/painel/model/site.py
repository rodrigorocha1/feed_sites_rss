from src.painel.model.config_base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Site(Base):

    __tablename__ = "SITE"

    ID_SITE = Column(Integer, primary_key=True, index=True, autoincrement=True)
    NOME_SITE = Column(String)
    noticias = relationship('Noticias', lazy='subquery')

    def __repr__(self):
        return f"SITE[ID_SITE={self.ID_SITE}, NOME_SITE={self.NOME_SITE}]"
