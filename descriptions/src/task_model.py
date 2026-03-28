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

class TaskTime(Enum):
    CUR_TIME = str(datetime.now())[:19]
    FINISH_TIME: str


class TaskFactory:
    """creating a task with calculating the ID and creation time"""
    def __init__(self):
        self._counter = 0
        self._created_time = TaskTime.CUR_TIME
    def create(self, task_description: str, priority: Priority, status: Status, finish_time: TaskTime):
        self._counter += 1
        finish_time = finish_time.strptime(finish_time, "%Y-%m-%d %H:%M:%S")
        return Task(self._counter, task_description, priority, status, self._created_time, finish_time)

class Task:
    """realisation task"""
    def __init__(self, id: int, task_description: str, priority: Priority, status: Status, finish_time: TaskTime, created_time: TaskTime):
        self.id = id
        self.task_description = task_description
        self.priority = priority
        self.status = status
        self.finish_time = finish_time
        self.created_time = created_time
        self.finish_time_ts = self.finish_time.timestamp()
        self.now_time = datetime.now().timestamp()

    def deadline_status(self) -> str:

        if self.now_time > self.finish_time_ts:
            return "task is overdue"
        if self.finish_time_ts < self.now_time + 86400:
            return "This is a hot task"
        else:
            return "Nice time to start this task"




