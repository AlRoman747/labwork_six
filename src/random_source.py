from src.find_source_tasks import Task
from random import randint


class RandomTaskGenerate:
    def __init__(self, seed=1):
        self.seed = seed
        self.tasks = {}
    def get_tasks(self) -> list[Task]:

        self.tasks.setdefault(self.seed, [])
        if self.tasks[self.seed]:
            return self.tasks[self.seed]
        else:
            for i in range(randint(1, 50)):
                self.tasks[self.seed].append(
                    {
                        "id": i,
                        "payload": f"task #{i}"
                    }
                )

        return self.tasks[self.seed]