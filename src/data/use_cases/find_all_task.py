from typing import Type
from src.domain.use_cases.find_all_tasks import FindAllTaskInterface
from src.data.interfaces.task_repository import TaskRepositoryInterface
from src.domain.models.task import Task

from src.errors.empty_task_list_error import EmptyTaskListError

class FindAllTask(FindAllTaskInterface):
    def __init__(self, task_repository: Type[TaskRepositoryInterface]) -> None:
        self.__task_repository = task_repository

    def find_all(self):
        tasks = self.__search_tasks()
        response = self.__format_response(tasks)
        print(response)
        return response

    def __search_tasks(self):
        tasks = self.__task_repository.get_all_tasks()
        if tasks == []:
            raise EmptyTaskListError('Empty task list')
        return tasks

    @classmethod
    def __format_response(cls, tasks: list[Task]):
        formatted_tasks = []
        for task in tasks:
            task_data = {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status
            }
            formatted_tasks.append(task_data)
        return f'tasks found successfully: {formatted_tasks}'
