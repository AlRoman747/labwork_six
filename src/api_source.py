from src.find_source_tasks import Task
from random import randint


class APISimulate:
    def __init__(self):
        self.priority_types = ['low', 'medium', 'high']
        self.data = [
            {"task_id": randint(0, 1000)} for i in range(10)
        ]
        for i in range(10):
            self.data[i].setdefault("task", f"task #{self.data[i]['task_id']}")
            self.data[i].setdefault("priority", self.priority_types[randint(0,2)])

    def get_tasks(self) -> list[Task]:
        tasks = []
        for item in self.data:
            tasks.append({
                "id": item["task_id"],
                "payload": {
                    "text": item["task"],
                    "priority": item["priority"],
                    "source": "api"
                }
            })
        return tasks