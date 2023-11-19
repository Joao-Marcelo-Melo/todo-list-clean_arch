from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.tasks import Tasks as TasksEntity
from src.data.interfaces.task_repository import TaskRepositoryInterface
from src.domain.models.task import Task
from src.infra.env.env_config import GetDbEnviroments

class TasksRepository(TaskRepositoryInterface):

    @classmethod
    def insert_task(cls, title : str, description : str, status=False) -> Task:
        with DBConnectionHandler(GetDbEnviroments()) as database:
            try:
                new_task = TasksEntity(
                    title=title,
                    description=description,
                    status=status
                )
                database.session.add(new_task)
                database.session.commit()
            except Exception as error:
                database.session.rollback()
                raise error

    @classmethod
    def get_task_by_id(cls, task_id : int) -> List[Task]:
        with DBConnectionHandler(GetDbEnviroments()) as database:
            try:
                tasks = (
                    database.session
                    .query(TasksEntity)
                    .filter(TasksEntity.id == task_id)
                )
                return tasks
            except Exception as error:
                database.session.rollback()
                raise error

    @classmethod
    def get_all_tasks(cls) -> List[Task]:
        with DBConnectionHandler(GetDbEnviroments()) as database:
            try:
                tasks = (
                    database.session
                    .query(TasksEntity)
                    .all()
                )
                return tasks
            except Exception as error:
                database.session.rollback()
                raise error

    @classmethod
    def delete_task_by_id(cls, task_id : int) -> None:
        with DBConnectionHandler(GetDbEnviroments()) as database:
            try:
                task_to_delete = (
                    database.session
                    .query(TasksEntity)
                    .filter(TasksEntity.id == task_id)
                    .first()
                )
                if task_to_delete:
                    database.session.delete(task_to_delete)
                    database.session.commit()
            except Exception as error:
                database.session.rollback()
                raise error
