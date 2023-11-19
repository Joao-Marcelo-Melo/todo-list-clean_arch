#pylint: disable=redefined-builtin
#pylint: disable=invalid-name

class Task:
    def __init__(self, id: int, title : str, description: str, status: bool) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.status = status
