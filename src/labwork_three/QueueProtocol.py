from typing import Protocol, Any, Iterator

from src.labwork_two.find_source_tasks import Task


class TaskQueue(Protocol):
    def add(self, task: Task) -> None:
        """adding tasks in queue"""
        ...


    def __iter__(self) -> Iterator[Task]:
        """rule for iterating in queue
        for loop automatically handle StopIteration"""
        ...


    def lazy_filter(self, param: Any, status: str) -> Iterator[Task]:
        """filter for any parameter from class Task from labwork two"""
        ...