from typing import List, Tuple, Any
from src.extracao.infa_banco.iinfra_banco import IInfraBanco
from src.pacote_log.config_log import logger
import os
import sqlite3


class ConexaoSqlite(IInfraBanco):

    def __init__(self) -> None:
        self.__caminho_raiz = os.getcwd()
        self.__caminho_banco = os.path.join(
            self.__caminho_raiz, 'scripts', 'noticias_rss.sqlite')
        self.__conexao = None
        self.__cursor = None

    def conectar_banco(self):
        try:
            self.__conexao = sqlite3.connect(self.__caminho_banco)
            self.__cursor = self.__conexao.cursor()
        except sqlite3.DatabaseError as msg:
            logger.error(f'Erro ao conectar no banco {msg}')
        except sqlite3.OperationalError as msg:
            logger.error(f'Falha de operação banco {msg}')
        except Exception as e:
            logger.critical(f'Falha Geral: {e}')

    def inserir_dados(self, tabela: str, colunas: Tuple[str], valores: List[Any]):

        placeholder = ', '.join('?' * len(valores))

        consulta = f"""
            INSERT INTO {tabela} {colunas}
            VALUES ({placeholder})
        """
        try:
            self.__cursor.execute(consulta, valores)
            self.__conexao.commit()
        except sqlite3.DataError as msg:
            logger.error(f'Erro ao inserir valor: {msg}')
        except sqlite3.IntegrityError as msg:
            pass

        except sqlite3.OperationalError as msg:
            logger.error(f'Error de operação: {msg}')
        except Exception as e:
            logger.critical(f'Falha geral {e}')

    def fechar_conexao(self):
        if self.__conexao:
            self.__cursor.close()
            self.__conexao.close()
