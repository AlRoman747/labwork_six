from src.labwork_two.find_source_tasks import Task



class ExecutorError(Exception):
    """Base class for executor errors"""
    pass

class TaskProcessingError(ExecutorError):
    """errors with correct Task"""
    def __init__(self, task: Task, cause: Exception):
        self.task = task
        self.cause = cause
        super().__init__(f"[{task.id}] {cause}")

    def __str__(self):
        return f"Task {self.task.id} failed: {self.cause}"


class ExecutorNotStartedError(ExecutorError):
    """Attempt to use executor before strat"""

    def __init__(self):
        super().__init__("Executor has not been started")