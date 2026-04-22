from collections import deque
from typing import Any, Iterator

from src.labwork_two.find_source_tasks import Task


class TaskQueue:
    def __init__(self):
        self._tasks = deque()

    def add(self, task: Task) -> None:
        """adding tasks in queue"""
        self._tasks.append(task)   # FIFO: добавляем вправо

    def pop(self):
        """removing tasks from queue"""
        if not self._tasks:
            raise IndexError("Queue is empty")
        return self._tasks.popleft()  # забираем слева

    def empty(self):
        return len(self._tasks) == 0

    def __len__(self):
        return len(self._tasks)

    def __iter__(self) -> Iterator:
        return iter(self._tasks)

    def lazy_filter(self, param: Any, status: str) -> Iterator:
        for task in self._tasks:
            if getattr(task, param).value == status:
                yield task