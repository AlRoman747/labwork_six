import pytest
from contract_programming.src import APISimulate
from contract_programming.src import RandomTaskGenerate


@pytest.mark.parametrize(
    "source_class",
    [APISimulate, RandomTaskGenerate]
)
def test_sources_structure(source_class):
    source = source_class()
    tasks = source.get_tasks()

    assert isinstance(tasks, list)
    assert len(tasks) > 0

    for task in tasks:
        assert isinstance(task, dict)
        assert "id" in task
        assert "payload" in task

