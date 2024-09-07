from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T1 = TypeVar('T1')
T2 = TypeVar('T2')


class IExtracao(ABC, Generic[T1, T2]):

    @abstractmethod
    def obter_dados(self) -> T1:
        pass

    @abstractmethod
    def extrair_dados(self, site: T1) -> T2:
        pass
