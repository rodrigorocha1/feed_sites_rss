from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Generator


T1 = TypeVar('T1')


class IRssExtracaoStrategy(ABC, Generic[T1]):

    @abstractmethod
    def obter_dados(self) -> T1:
        pass

    @abstractmethod
    def extrair_dados(self, site: T1) -> Generator[Dict[str, str], None, None]:
        pass
