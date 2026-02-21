from find_source_tasks import *


def check_source(source) -> str:
    if isinstance(source, TaskSource):
        return f"{source.__class__.__name__}: Контракт соблюден"

    raise TypeError(f"{source.__class__.__name__}: Контракт не соблюден")

