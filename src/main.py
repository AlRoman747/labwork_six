from src.labwork_one.check_source import SourceChecker
from src.labwork_one.random_source import RandomTaskGenerate
from src.labwork_one.file_source import ReadFromFile
from src.labwork_one.api_source import APISimulate
from src.labwork_two.find_source_tasks import TaskFactory
from src.labwork_three.task_queue import TaskQueue



def main():
    sources = [
        RandomTaskGenerate,
        ReadFromFile,
        APISimulate
    ]

    print("-----------labwork 1-------------------")
    for source in sources:
        checker = SourceChecker(source())
        print(checker.check_source())
    print("-----------labwork 2-------------------")
    factory = TaskFactory()
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
    print("-----------labwork 3-------------------")
    task_queue = TaskQueue()
    task_one = factory.create("test1", "low", "in progress", "2026-03-30 00:00:00")
    task_two = factory.create("test2", "low", "in progress", "2026-03-30 00:00:00")
    task_three = factory.create("test3", "high", "in progress", "2036-03-30 00:00:00")
    task_queue.add(task_one)
    task_queue.add(task_two)
    task_queue.add(task_three)

    tasks = [str(i) for i in list(task_queue.lazy_filter("priority", "low"))]
    print(tasks)
    print(list(task_queue))
    for i in task_queue:
        print(i)
    print("-----------labwork 4-------------------")

if __name__ == "__main__":
    main()
