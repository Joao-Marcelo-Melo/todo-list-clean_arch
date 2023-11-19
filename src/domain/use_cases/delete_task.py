from abc import ABC, abstractmethod

class DeleteTask(ABC):

    @abstractmethod
    def delete(self, task_id : int) -> None:
        pass
