from typing import Protocol, runtime_checkable


@runtime_checkable
class Task(Protocol):
    id: int
    payload: object

@runtime_checkable
class API_Task(Protocol):
    id: int
    payload: object


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        """ Возвращает список задач"""
        pass