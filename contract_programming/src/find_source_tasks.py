from typing import Protocol, runtime_checkable, TypedDict, Any


class Task(TypedDict):
    id: int
    payload: Any


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        """ Возвращает список задач"""
        pass