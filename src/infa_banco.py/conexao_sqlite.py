from typing import List, Tuple, Any
from .iinfra_banco import IInfraBanco
import os
import sqlite3


class ConexaoSqlite(IInfraBanco[sqlite3.Connection]):

    def __init__(self) -> None:
        self.__caminho_raiz = os.getcwd()
        self.__caminho_banco = os.path.join(
            self.__caminho_raiz, 'scripts', 'noticias_rss.sqlite')
        self.__conexao = None
        self.__cursor = None

    def conectar_banco(self):
        self.__conexao = sqlite3.connect(self.__caminho_banco)
        self.__cursor = self.__conexao.cursor()

    def inserir_dados(self, tabela: str, colunas: Tuple[str], valores: List[Any]):
        if not self.__conexao or not self.__cursor:
            self.conectar_banco()
        consulta = """

        """
        self.__cursor.execute(consulta, valores)
        self.__conexao.commit()

    def fechar_conexao(self):
        if self.__conexao:
            self.__cursor.close
            self.__conexao.close

    def __enter__(self):
        self.conectar_banco()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.fechar_conexao()

    def __del__(self):
        self.fechar_conexao()
