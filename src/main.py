from src.check_source import SourceChecker
from src.labwork_one.random_source import RandomTaskGenerate
from src.labwork_one.file_source import ReadFromFile
from src.labwork_one.api_source import APISimulate
from find_source_tasks import TaskFactory


def main():
    sources = [
        RandomTaskGenerate,
        ReadFromFile,
        APISimulate
    ]


    for source in sources:
        checker = SourceChecker(source())
        print(checker.check_source())

    '''
    factory = TaskFactory()
    task = factory.create("make labwork", "high", "in progress","2026-03-29 19:00:00") # "%Y-%m-%d %H:%M:%S"
    print(task.deadline_status)
    print(task.id) # assert id == 1
    # task.id = 4 # assert error
    task = factory.create("make homework", "medium", "in progress","2026-03-30 19:00:00") # "%Y-%m-%d %H:%M:%S"
    print(task.id)
    print(task.priority()) # assert medium
    print(str(task))
'''


if __name__ == "__main__":
    main()