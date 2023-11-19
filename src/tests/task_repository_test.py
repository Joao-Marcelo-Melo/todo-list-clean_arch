#import pytest
from src.infra.db.repositories.task_repository import TasksRepository

#@pytest.mark.skip(reason="Sensive test")
def test_insert_task():
    mocked_title = 'fazer café'
    mocked_description = 'fazer cafe com acuca e leite'

    task_repository = TasksRepository()
    task_repository.insert_task(mocked_title, mocked_description)
