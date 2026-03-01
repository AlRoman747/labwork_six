from src.find_source_tasks import Task
import json


class ReadFromFile:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    def get_tasks(self)  -> list[Task]:
        try:
            with open(self.filename) as file: return json.load(file)

        except FileNotFoundError: raise FileNotFoundError(f"Файл {self.filename} не найден")
