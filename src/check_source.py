from src.find_source_tasks import TaskSource


class SourceChecker:
    def __init__(self, source):
        self.source = source

    def check_source(self) -> str:

        if not isinstance(self.source, TaskSource):
            raise TypeError(f"{self.source.__class__.__name__}: Контракт не соблюдён")

        tasks = self.source.get_tasks()


        if not isinstance(tasks, list):
            raise TypeError(f"{tasks.__class__.__name__}: Контракт не соблюдён")

        for task in tasks:
            if not isinstance(task, dict):
                raise TypeError(f"{task.__class__.__name__}: Контракт не соблюдён")

        return f"{self.source.__class__.__name__}: Контракт соблюдён"