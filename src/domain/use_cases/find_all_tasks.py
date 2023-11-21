from abc import ABC, abstractmethod
from typing import Dict

class FindAllTaskInterface(ABC):

    @abstractmethod
    def find_all(self) -> Dict:
        pass
