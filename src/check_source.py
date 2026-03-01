from find_source_tasks import TaskSource


def check_source(source) -> str:
    tasks = source.get_tasks()

    if not isinstance(tasks, list):
        raise TypeError(f"{source.__class__.__name__}: Контракт не соблюден")

    for task in tasks:
        if not isinstance(task, dict) or "id" not in task or "payload" not in task:
            raise TypeError(f"{source.__class__.__name__}: Контракт не соблюден")

    return f"{source.__class__.__name__}: Контракт соблюден"

