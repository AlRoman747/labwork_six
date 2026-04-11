from src.labwork_two.find_source_tasks import TaskFactory

factory = TaskFactory()
task_one = factory.create("test1", "low", "in progress", "2026-03-30 00:00:00")
task_two = factory.create("test2", "low", "in progress", "2026-03-30 00:00:00")

def test_correct_priority():
    """check what priority exist, after changing id on correct everything good, but after changing to incorrect..."""
    test_data = [task_one.priority.value, task_two.priority.value]

    assert test_data[0] == test_data[1]
    try:
        task_one.priority = "high"
        assert task_one.priority != task_two.priority
        task_one.priority = "middle"
    except Exception as e:
        assert type(e) is ValueError