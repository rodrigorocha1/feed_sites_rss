from abc import ABC, abstractmethod
from typing import Tuple, List, Any, Generic, TypeVar


T = TypeVar('T')


class IInfraBanco(ABC, Generic[T]):
    @ abstractmethod
    def conectar_banco(self) -> bool, T:
        """Método para conectar no banco

        Returns:
            bool: Verdadeiro se conectou no banco
        """
        pass

    def inserir_dados(self, tabela: str, colunas: Tuple[str], valores: List[Any]):
        """Método para inserir dados no banco

        Args:
            tabela (str): Nome da tabela no banco
            colunas (Tuple[str]): As colunas no banco
            valores (List[Any]): Valores que serão efetivamente amarzenado
        """
        pass

    def fechar_conexao(self):
        """Método para fechar a conexão
        """
        pass
