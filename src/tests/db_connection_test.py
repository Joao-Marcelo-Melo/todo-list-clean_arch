import pytest
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.env.env_config import GetDbEnviroments

@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection_handle = DBConnectionHandler(GetDbEnviroments())
    engine = db_connection_handle.get_engine()
    assert engine is not None
