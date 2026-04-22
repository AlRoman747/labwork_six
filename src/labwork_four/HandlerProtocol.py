from typing import Protocol, runtime_checkable
from src.labwork_two.find_source_tasks import Task



@runtime_checkable
class TaskHandler(Protocol):
    """Handle task to worker"""

    async def handle(self, task: Task) -> None:
        """process the task"""
        ...