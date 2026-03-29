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
    print("-----------labwork 2-------------------")
    print(f"Hello. Here you can create task\nIf u wanna stop any time just type exit")

    while a := input() != 'exit':
        task_source = []
        print("Lets start with description your task. Tell me about that u gonna do")
        task_source.append(input())
        print("Lets move on and now tell me how important this task for you: choose from: low, medium, high")
        task_source.append((input()))
        print("Now tell me what on what level ur task: open, in progress, in review, testing, blocked or done")
        task_source.append(input())
        print('And finally in format "%Y-%m-%d %H:%M:%S" tell me when you gonna done ur task')
        task_source.append(input())
        try:
            task = factory.create(task_source[0], task_source[1], task_source[2], task_source[3])
            print(f"here your task: {str(task)}")
            print("type y if u wanna check ur deadline status")
            if input() == "y":
                print(task.deadline_status)
        except Exception as e:
            print("oooops... happened smth bad...", e)
if __name__ == "__main__":
    main()