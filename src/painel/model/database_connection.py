from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.painel.model.noticias import Base
import os


class DatabaseConnection:

    def __init__(self) -> None:
        self.__DATABASE_URL = os.path.join(
            os.getcwd(), 'scripts', 'noticias_rss.sqlite')
        self.engine = create_engine(self.__DATABASE_URL, echo=True)
        self.SessionLocal = sessionmaker(
            autocomit=False, autoflush=False, bind=self.engine)

    def obter_sessao(self):
        return self.SessionLocal()

    def iniciar_banco(self):
        Base.metadata.create_all(bind=self.engine)
