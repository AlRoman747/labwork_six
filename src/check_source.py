from find_source_tasks import TaskSource


def check_source(source) -> str:

    if not isinstance(source, TaskSource):
        raise TypeError(f"{source.__class__.__name__}: Контракт не соблюдён")

    tasks = source.get_tasks()


    if not isinstance(tasks, list):
        raise TypeError(f"{tasks.__class__.__name__}: Контракт не соблюдён")

    for task in tasks:
        if not isinstance(task, dict):
            raise TypeError(f"{task.__class__.__name__}: Контракт не соблюдён")

    return f"{source.__class__.__name__}: Контракт соблюдён"