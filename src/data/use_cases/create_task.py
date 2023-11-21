from typing import Type
from src.domain.use_cases.create_task import CreateTaskInterface
from src.data.interfaces.task_repository import TaskRepositoryInterface

from src.errors.http_bad_request import HttpBadRequestError

class CreateTask(CreateTaskInterface):
    def __init__(self, task_repository : Type[TaskRepositoryInterface]) -> None:
        self.__task_repository = task_repository

    def create(self, title : str, description : str):
        self.__validate_task(title)
        self.__validate_task(description)

        self.__create_task(title, description)
        response = self.__format_response(title, description)
        return response

    @classmethod
    def __validate_task(cls, info):
        if not isinstance(info, str):
            raise ValueError('Task Title must be an String')

    def __create_task(self, title : str, description : str):
        task = self.__task_repository.insert_task(title, description)
        if task == []:
            raise HttpBadRequestError('Unable to create task')
        return task

    @classmethod
    def __format_response(cls, title : str, description : str):
        response = {
            "title" : title,
            "description" : description
        }
        return f'task created successfully: {response}'
