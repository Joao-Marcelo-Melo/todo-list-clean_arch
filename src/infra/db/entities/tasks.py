from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import Base

class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    status = Column(bool, nullable=False)

    def __repr__(self):
        return f'Tasks [id={self.id}, description[{self.description}, status={self.status}]]'
