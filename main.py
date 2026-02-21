from typing import Protocol, runtime_checkable


@runtime_checkable
class Tasks(Protocol):
    def