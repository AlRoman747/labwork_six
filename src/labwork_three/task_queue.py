import copy
from typing import Iterable
import queue
from typing import Any, Iterator

from src.labwork_two.find_source_tasks import Task


class TaskQueue:
    def __init__(self):
        """ create an empty queue from collections framework"""
        self._tasks = queue.Queue()


    def add(self, task: Task) -> None:
        """adding tasks in queue"""
        self._tasks.put(task)

    def pop(self) -> None:
        """removing tasks from queue"""
        if not self._tasks:
            raise IndexError("Queue is empty")
        return self._tasks.get()

    def empty(self):
        return self._tasks.empty()

    def __len__(self):
        return self._tasks.qsize()

    def __iter__(self):
        return self
    def __next__(self):
        task = self._tasks.get()
        self.


    def lazy_filter(self, param: Any, status: str) -> Iterator[Task]:
        """filter for any parameter from class Task from labwork two"""
        for task in self._tasks:
            if getattr(task, param).value == status:
                yield task
