from typing import Protocol, runtime_checkable, TypedDict, Any
from datetime import datetime
from src.labwork_two.priority import Priority
from src.labwork_two.status import Status


class EnumDescriptor:
    def __init__(self, enum_class):
        self.enum_class = enum_class

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, f"_{self.name}")

    def __set__(self, instance, value):
        try:
            # Проверяем, что value — член enum_class
            enum_value = self.enum_class(value)
        except Exception:
            raise ValueError(f"{value} not avaliable for {self.enum_class.__name__}")
        setattr(instance, f"_{self.name}", enum_value)

class FinishTimeDescriptor:
    """Description for manage and validate task finish time."""
    def __set_name__(self, owner, name):
        """Save name attribute for work with _finish_time"""
        self.name = name
        self.internal_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # return attribute value
        return getattr(instance, self.internal_name)

    def __set__(self, instance, value):
        try:
            parsed_dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            setattr(instance, self.internal_name, parsed_dt)
        except (ValueError, TypeError):
            raise ValueError("Finish time must be in format 'YYYY-MM-DD HH:MM:SS'")


class Task:
    """realisation task"""
    priority = EnumDescriptor(Priority)
    status = EnumDescriptor(Status)
    finish_time = FinishTimeDescriptor()

    def __init__(self, task_id: int, description: str, priority: Priority, status: Status, finish_time: datetime, created_time: datetime):
        self._id = task_id
        self._description = description
        self.priority = priority
        self.status = status
        self._finish_time = finish_time
        self._created_time = created_time

    @property
    def id(self) -> str:
        return f"#{self._id}"


    def description(self) -> str:
        return self._description


    @property
    def created_time(self) -> datetime:
        return self._created_time


    @property
    def deadline_status(self) -> str:
        now_ts = datetime.now().timestamp()
        finish_ts = self._finish_time.timestamp()
        if now_ts > finish_ts:
            return "task is overdue"
        elif finish_ts < now_ts + 86400:
            return "This is a hot task"
        else:
            return "Nice time to start this task"

    def __str__(self):
        return (f'Task {self._id} "{self._description}", status: {self.status.value}, priority: {self.priority.value}, finish at: {self._finish_time}')


class TaskFactory:
    """creating a task with calculating the ID and creation time"""
    def __init__(self):
        self._counter = 0

    def create(self, description: str, priority: Priority, status: Status,
               finish_time: str) -> Task:
        self._counter += 1
        try:
            finish_dt = datetime.strptime(finish_time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Finish time must be in format 'YYYY-MM-DD HH:MM:SS'")
        created_dt = datetime.now()
        return Task(self._counter, description, priority, status, finish_dt, created_dt)


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        """ Возвращает список задач"""
        pass