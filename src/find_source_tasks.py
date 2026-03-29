from typing import Protocol, runtime_checkable, TypedDict, Any
from datetime import datetime
from src.labwork_two.priority import Priority
from src.labwork_two.status import Status



class TaskFactory:
    """creating a task with calculating the ID and creation time"""
    def __init__(self):
        self._counter = 0
    def create(self, task_description: str, priority: Priority, status: Status, finish_time: str):
        self._counter += 1
        try:
            finish_dt  = datetime.strptime(finish_time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return "enter finish time in format YEAR-MONTH-DAY HOUR:MINUTES:SECONDS"
        created_dt = datetime.now()

        return Task(
            self._counter,
            task_description,
            priority,
            status,
            finish_dt,
            created_dt
        )

class Task:
    """realisation task"""
    def __init__(self, id: int, task_description: str, priority: Priority, status: Status, created_time: datetime, finish_time: datetime):
        self.__id = id
        self.__task_description = task_description
        self.__priority = priority
        self.__status = status
        self._finish_time = finish_time
        self._created_time = created_time
        self._finish_time_ts = self._finish_time.timestamp()

    @property
    def deadline_status(self) -> str:
        now = datetime.now().timestamp()
        """simple calculating task state. Can be upgrade by using status and priority"""
        if now > self._finish_time_ts:
            return "task is overdue"
        if self._finish_time_ts < now + 86400:
            return "This is a hot task"
        else:
            return "Nice time to start this task"


    @property
    def id(self) -> str:
        return f'#{self.__id}'


    def description(self) -> str:
        return self.__task_description


    def priority(self) -> str:
        return self.__priority


    def status(self) -> str:
        return self.__status

    def __str__(self):
        return f'Task #{self.__id} "{self.__task_description}", status: {self.__status}, priority: {self.__priority}, finish at: {self._finish_time}'


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        """ Возвращает список задач"""
        pass