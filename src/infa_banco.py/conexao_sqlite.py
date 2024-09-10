from iinfra_banco import IInfraBanco
import os


class ConexaoSqlite(IInfraBanco):

    def __init__(self) -> None:
        self.__caminho_raiz = os.getcwd()
