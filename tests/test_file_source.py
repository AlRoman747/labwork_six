from src.file_source import ReadFromFile
import json


def test_read_file(tmp_path):
    test_data = [
        {"id": 1, "payload": "test task 1"},
        {"id": 2, "payload": "test task 2"}
    ]

    json_file = tmp_path / "tasks.json"
    json_file.write_text(json.dumps(test_data))

    reader = ReadFromFile(filename=str(json_file))
    tasks = reader.get_tasks()

    assert tasks == test_data


