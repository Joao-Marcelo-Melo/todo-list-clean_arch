import pytest
from sqlalchemy import text

from src.infra.db.repositories.task_repository import TasksRepository
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.env.env_config import GetDbEnviroments

db_connection_handler = DBConnectionHandler(GetDbEnviroments())
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive test")
def test_insert_task():
    mocked_title = 'refactor code'
    mocked_description = 'refactor code to go into production'

    task_repository = TasksRepository()
    task_repository.insert_task(mocked_title, mocked_description)

    sql = '''
        SELECT * FROM tasks
        WHERE title = '{}'
        AND description = '{}'
    '''.format(mocked_title, mocked_description)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.title == mocked_title
    assert registry.description == mocked_description

    connection.execute(text(f'''
        DELETE FROM tasks WHERE id = {registry.id}
    '''))
    connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_select_task_by_id():
    mocked_id = 3
    mocked_title = 'refactor code'
    mocked_description = 'refactor code to go into production'
    mocked_status = False

    sql = '''
        INSERT INTO tasks (id, title, description, status) VALUES ('{}', '{}', '{}', {})
    '''.format(mocked_id, mocked_title, mocked_description, mocked_status)
    connection.execute(text(sql))
    connection.commit()

    task_repository = TasksRepository()
    tasks = task_repository.get_task_by_id(mocked_id)

    assert tasks[0].id == mocked_id

    connection.execute(text(f'''
         DELETE FROM tasks WHERE id = {tasks[0].id}
     '''))
    connection.commit()
