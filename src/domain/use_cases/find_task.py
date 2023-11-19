from abc import ABC, abstractmethod
from typing import Dict

class FindTaskInterface(ABC):

    @abstractmethod
    def find(self, task_id : int) -> Dict:
        pass
