from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any


T1 = TypeVar('T1')
T2 = TypeVar('T2')


class IRssExtracaoStrategy(ABC, Generic[T1]):

    @abstractmethod
    def obter_dados(self) -> T1:
        pass

    @abstractmethod
    def extrair_dados(self, site: T1) -> Any:
        pass
