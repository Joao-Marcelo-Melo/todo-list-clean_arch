from typing import Type
from src.domain.use_cases.find_task import FindTaskInterface
from src.data.interfaces.task_repository import TaskRepositoryInterface
from src.domain.models.task import Task

from src.errors.http_bad_request import HttpBadRequestError

class FindTask(FindTaskInterface):
    def __init__(self, task_repository : Type[TaskRepositoryInterface]) -> None:
        self.__task_repository = task_repository

    def find(self, task_id):
        self.__validate_task(task_id)
        task = self.__search_task(task_id)
        response = self.__format_response(task)
        print(response)
        return response

    @classmethod
    def __validate_task(cls, task_id):
        if not isinstance(task_id, int):
            raise ValueError('Task ID must be an integer')

    def __search_task(self, task_id):
        task = self.__task_repository.get_task_by_id(task_id)
        if task == []:
            raise HttpBadRequestError('Not Found Task ID')
        return task[0]

    @classmethod
    def __format_response(cls, task : Task):
        response = {
            "id" : task.id,
            "title" : task.title,
            "description" : task.description,
            "status" : task.status
        }
        return response
