from abc import ABC, abstractmethod
from typing import Tuple, List, Any


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
