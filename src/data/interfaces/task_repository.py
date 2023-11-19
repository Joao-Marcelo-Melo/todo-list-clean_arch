from typing import List
from abc import ABC, abstractmethod
from src.domain.models.task import Task

class TaskRepositoryInterface(ABC):

    @abstractmethod
    def insert_task(self, title : str , description : str, status : bool) -> Task:
        pass

    @abstractmethod
    def get_task_by_id(self, task_id : int) -> List[Task]:
        pass

    @abstractmethod
    def get_all_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def delete_task_by_id(self, task_id : int) -> None:
        pass
