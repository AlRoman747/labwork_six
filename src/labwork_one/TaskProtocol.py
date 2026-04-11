from typing import runtime_checkable, Protocol
from src.labwork_two.find_source_tasks import Task


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        """ return tasks list"""
        pass