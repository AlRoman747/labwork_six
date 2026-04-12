from src.labwork_two.find_source_tasks import TaskFactory
from src.labwork_two.find_source_tasks import Task
from src.labwork_three.task_queue import TaskQueue

factory = TaskFactory()
task_one = factory.create("test1", "low", "in progress", "2026-01-30 00:00:00")
task_two = factory.create("test2", "low", "in progress", "2036-03-30 00:00:00")
task_three = factory.create("test3", "high", "in progress", "2036-03-30 00:00:00")
test_queue = TaskQueue()
test_queue.add(task_one)
test_queue.add(task_two)
test_queue.add(task_three)

def test_iterations():
    for i in test_queue:
        assert isinstance(i, Task)
def test_incorrect_iteration():
    queue = 748
    try:
        for i in queue:
            assert False
    except TypeError as e:
        assert e
def test_twice_in_queue():
    for i in test_queue:
        for j in test_queue:
            assert isinstance(i, Task)
            assert isinstance(j, Task)

def test_list():
    try:
        test_list = list(test_queue)
        assert isinstance(test_list, list)
    except Exception as _:
        assert False

def test_fileter():
    tasks = [str(i) for i in list(test_queue.lazy_filter("priority", "low"))]

    assert len(tasks) == 2 and len(tasks) < len(list(test_queue))

    for i in tasks:
        assert 'priority: low' in i
