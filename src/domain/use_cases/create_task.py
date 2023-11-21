from abc import ABC, abstractmethod
from typing import Dict

class CreateTaskInterface(ABC):

    @abstractmethod
    def create(self, title : str, description : str, status=False) -> Dict:
        pass
