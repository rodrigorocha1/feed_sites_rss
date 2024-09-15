from src.painel.model.config_base import Base
from sqlalchemy import Column, Integer, String


class Site(Base):

    __tablename__ = "SITE"

    ID_SITE = Column(Integer, primary_key=True, index=True, autoincrement=True)
    NOME_SITE = Column(String)
