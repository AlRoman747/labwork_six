from src.labwork_two.find_source_tasks import TaskFactory

factory = TaskFactory()
task_one = factory.create("test1", "low", "in progress", "2026-03-30 00:00:00")
task_two = factory.create("test2", "low", "in progress", "2026-03-30 00:00:00")

def test_correct_id():
    """check what id exist, next id bigger than previous and what user cannot change id"""
    test_data = [int(task_one.id[1:]), int(task_two.id[1:])]

    assert test_data[0] == 1
    assert test_data[0] < test_data[1]
    try:
        task_one.id = 4
    except Exception as e:
        assert type(e) is AttributeError
