from typing import Protocol, runtime_checkable, TypedDict

class Task(TypedDict):
    id: int
    payload: str


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        """ Возвращает списоко задач"""
        pass