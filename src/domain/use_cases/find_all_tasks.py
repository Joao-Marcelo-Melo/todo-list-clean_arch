from abc import ABC, abstractmethod
from typing import Dict

class FindTask(ABC):

    @abstractmethod
    def find(self) -> Dict:
        pass
