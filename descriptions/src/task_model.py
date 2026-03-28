from datetime import datetime
from enum import Enum


class Priority(Enum):
    """fields for priority types"""
    LOW="low"
    MEDIUM="medium"
    HIGH="high"

class Status(Enum):
    """fields for status types"""
    OPEN = "open"
    IN_PROGRESS = "in progress"
    IN_REVIEW = "in review"
    TESTING = "testing"
    BLOCKED = "blocked"
    DONE = "done"

class CurrentTime(Enum):
    TIME = str(datetime.now())[:19]

class TaskFactory:
    """creating a task with calculating the ID and creation time"""
    def __init__(self):
        self._counter = 0
        self._time = CurrentTime.TIME
    def create(self, task_description: str, priority: Priority, status: Status):
        self._counter += 1

        return Task(self._counter, task_description, priority, status, self._time)

class Task:
    """realisation task"""
    def __init__(self, id: int, task_description: str, priority: Priority, status: Status, created_time: CurrentTime):
        self.id = id
        self.task_description = task_description
        self.priority = priority
        self.status = status
        self.created_time = created_time


