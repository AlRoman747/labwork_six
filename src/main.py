from check_source import SourceChecker
from random_source import RandomTaskGenerate
from file_source import ReadFromFile
from api_source import APISimulate
from find_source_tasks import Task, TaskFactory


def main():
    sources = [
        RandomTaskGenerate,
        ReadFromFile,
        APISimulate
    ]


    for source in sources:
        checker = SourceChecker(source())
        print(checker.check_source())

    """
    factory = TaskFactory()
    task = factory.create("make labwork", "high", "in progress","2026-03-29 19:00:00") # "%Y-%m-%d %H:%M:%S"
    deadline = task.deadline_status()
    print(deadline)
    """


if __name__ == "__main__":
    main()