from src.labwork_two.find_source_tasks import TaskFactory

factory = TaskFactory()
task_one = factory.create("test1", "low", "in progress", "2026-01-30 00:00:00")
task_two = factory.create("test2", "low", "in progress", "2036-03-30 00:00:00")

def test_correct_date_checker():
    """check what deadline work correctly, what if user create task with correct finish time everything good, but if with incorrect...
    also check what happened after date changing"""
    test_data = [task_one.deadline_status, task_two.deadline_status]

    assert test_data[0] == "task is overdue"
    assert test_data[1] == "Nice time to start this task"

    try:
        task_one.finish_time = "2026-11-30 00:00:00"
        assert task_one.deadline_status == "Nice time to start this task"
        task_three = factory.create("test3", "low", "in progress", "2036/03/30 00:00:00")
    except Exception as e:
        assert type(e) is ValueError