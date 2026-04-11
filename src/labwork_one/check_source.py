from src.labwork_one.TaskProtocol import TaskSource


class SourceChecker:
    def __init__(self, source):
        self.source = source

    def check_task(self, task: dict) -> bool:
        """Check type task"""
        return (
                isinstance(task, dict)
                and "id" in task
                and isinstance(task["id"], int)
                and "payload" in task
        )

    def check_source(self) -> str:
        """Check Protocol"""
        if not isinstance(self.source, TaskSource):
            raise TypeError(f"{self.source.__class__.__name__}: Protocol was not followed")

        tasks = self.source.get_tasks()


        if not isinstance(tasks, list):
            raise TypeError(f"{tasks.__class__.__name__}: Protocol was not followed")

        for task in tasks:
            if not self.check_task(task):
                raise TypeError(f"{task.__class__.__name__}: Protocol was not followed")

        return f"{self.source.__class__.__name__}: Protocol has been followed"