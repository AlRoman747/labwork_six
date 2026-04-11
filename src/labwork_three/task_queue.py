from datetime import datetime
from typing import Any, Iterator

from src.labwork_two.find_source_tasks import Task


class TaskQueue:
    def __init__(self) -> None:
        """create list for queue"""
        self._tasks = list()


    def add(self, task: Task) -> None:
        """adding tasks in queue"""
        self._tasks.append(task)


    def __iter__(self) -> Iterator[Task]:
        """rule for iterating in queue
        for loop automatically handle StopIteration"""
        for task in self._tasks:
            yield task


    def lazy_filter(self, param: Any, status: str) -> Iterator[Task]:
        """filter for any parameter from class Task from labwork two"""
        for task in self._tasks:
            if getattr(task, param).value == status:
                yield task
