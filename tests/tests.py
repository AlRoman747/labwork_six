import pytest
from src.find_source_tasks import RandomTaskGenerate, ReadFromFile, APISimulate
import json
from pathlib import Path


def test_api():
    api_plug = APISimulate()
    assert type(api_plug.get_tasks()) is list
    assert type(api_plug.get_tasks()[0]) is dict

def test_generator():
    generator = RandomTaskGenerate()
    assert type(generator.get_tasks()) is list
    assert type(generator.get_tasks()[0]) is dict

def test_read_file():
    test_data = [
        {"id": 1, "payload": "test task 1"},
        {"id": 2, "payload": "test task 2"}
    ]
    json_file = Path.cwd() / "tasks.json"
    with open(json_file, 'w') as f:
        json.dump(test_data, f)

    reader = ReadFromFile(filename=str(json_file))
    tasks = reader.get_tasks()

    assert tasks == test_data
