import json
from random import randint

class RandomTaskGenerate:
    def get_tasks(self) -> list:
        tasks = []

        for i in range(randint(1, 50)):
            tasks.append(
                {
                    "id": i,
                    "payload": f"task #{i}"
                }
            )

        return tasks


class ReadFromFile:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def get_tasks(self):
        try:
            with open(self.filename) as file: return json.load(file)

        except FileNotFoundError: return "Введите корректное название файла"



class APISimulate:
    def __init__(self):
        self.priority_types = ['low', 'medium', 'high']
        self.data = [
            {"task_id": randint(0, 1000)} for i in range(10)
        ]
        for i in range(10):
            self.data[i].setdefault("task", f"task #{self.data[i]['task_id']}")
            self.data[i].setdefault("priority", self.priority_types[randint(0,2)])

    def get_tasks(self) -> list:
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



GEN = APISimulate()
print(GEN.get_tasks())