from typing import Type
from src.domain.use_cases.delete_task import DeleteTaskInterface
from src.data.interfaces.task_repository import TaskRepositoryInterface

from src.errors.http_bad_request import HttpBadRequestError

class DeleteTask(DeleteTaskInterface):
    def __init__(self, task_repository : Type[TaskRepositoryInterface]) -> None:
        self.__task_repository = task_repository

    def delete(self, task_id : int):
        self.__validate_task(task_id)
        self.__delete_task(task_id)
        response = self.__format_response(task_id)
        return response

    @classmethod
    def __validate_task(cls, task_id):
        if not isinstance(task_id, int):
            raise ValueError('Task ID must be an integer')

    def __delete_task(self, task_id):
        task = self.__task_repository.delete_task_by_id(task_id)
        if task == []:
            raise HttpBadRequestError('Unable to deleted task')
        return task

    @classmethod
    def __format_response(cls, task_id):
        response = {
            "task_id" : task_id
        }
        return f'task deleted successfully: {response}'
