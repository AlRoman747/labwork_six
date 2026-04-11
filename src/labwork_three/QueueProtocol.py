from typing import Protocol, Any

from src.labwork_two.find_source_tasks import Task


class TaskQueue(Protocol):
    def __iter__(self):
        """iterations rules to iterate by task queue"""
        ...
    '''
    def filter(self, param: Any) -> Task:
        """rules for tasks lazy filtration by params what were released in lab work two"""
        ...
    def __add__(self, other):
    '''