from src.find_source_tasks import Task
from random import randint


class RandomTaskGenerate:
    def get_tasks(self) -> list[Task]:
        tasks = []

        for i in range(randint(1, 50)):
            tasks.append(
                {
                    "id": i,
                    "payload": f"task #{i}"
                }
            )

        return tasks