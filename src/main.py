from src.check_source import SourceChecker
from src.labwork_one.random_source import RandomTaskGenerate
from src.labwork_one.file_source import ReadFromFile
from src.labwork_one.api_source import APISimulate
from find_source_tasks import TaskFactory
from labwork_two.status import Status
from labwork_two.priority import Priority


def main():
    sources = [
        RandomTaskGenerate,
        ReadFromFile,
        APISimulate
    ]


    for source in sources:
        checker = SourceChecker(source())
        print(checker.check_source())
    factory = TaskFactory()
    task = factory.create("Write lab report", "high", "in progress", "2026-03-29 20:00:00")

    print(task.status)  # Status.IN_PROGRESS
    task.status = "open"
    print(task.status)

if __name__ == "__main__":
    main()