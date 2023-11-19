from typing import Type
from pydantic_settings import BaseSettings, SettingsConfigDict

class DbEnviroments(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', case_sensitive=False)
    user : str
    password : str
    host : str
    port : int
    db_name : str

class SetDbEnviroments:
    def __init__(self, db_enviroments : Type[DbEnviroments]) -> None:
        user = db_enviroments.user
        password = db_enviroments.password
        host = db_enviroments.host
        port = db_enviroments.port
        db_name = db_enviroments.db_name
        self.connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(
            user,
            password,
            host,
            port,
            db_name
        )

class GetDbEnviroments:
    def __get_config(self):
        db_enviroments = DbEnviroments()
        return SetDbEnviroments(db_enviroments)

    def get_engine(self):
        config = self.__get_config()
        return config.connection_string
