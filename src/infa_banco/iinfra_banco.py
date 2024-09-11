from abc import ABC, abstractmethod
from typing import Tuple, List


class IInfraBanco(ABC,):

    @abstractmethod
    def conectar_banco(self):
        pass

    @abstractmethod
    def inserir_dados(self, tabela: str, colunas: Tuple[str], valores: List[Any]):
        """Método para inserir dados no banco

        Args:
            tabela (str): Nome da tabela no banco
            colunas (Tuple[str]): As colunas no banco
            valores (List[Any]): Valores que serão efetivamente amarzenado
        """
        pass

    @abstractmethod
    def fechar_conexao(self):
        """Método para fechar a conexão
        """
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @abstractmethod
    def __del__(self):
        pass
