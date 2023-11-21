from abc import ABC, abstractmethod

class DeleteTaskInterface(ABC):

    @abstractmethod
    def delete(self, task_id : int) -> None:
        pass
