from src.find_source_tasks import TaskFactory, Task

factory = TaskFactory()
task_one = factory.create("test1", "low", "in progress", "2026-03-30 00:00:00")
task_two = factory.create("test2", "low", "in progress", "2026-03-30 00:00:00")

def test_correct_status():
    """check what status exist, after changing id on correct everything good, but after changing to incorrect..."""
    test_data = [task_one.status.value, task_two.status.value]

    assert test_data[0] == test_data[1]
    try:
        task_one.status = "open"
        assert  task_one.status != task_two.status
        task_one.status = "close"
    except Exception as e:
        assert type(e) is ValueError