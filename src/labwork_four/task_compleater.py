import asyncio

from src.labwork_four.HandlerProtocol import TaskHandler
from src.labwork_four.errors_handlers import TaskProcessingError, ExecutorNotStartedError, ExecutorError
from src.labwork_two.find_source_tasks import Task


class AsyncTaskExecutor:
    """Async task executor.

    Example::

        async with AsyncTaskExecutor(workers=3) as executor:
            executor.register_handler(MyHandler())
            await executor.submit(task)
            await executor.wait_all()
    """

    def __init__(self, workers: int = 2) -> None:
        """Args:
           workers: number of parallel worker-coroutine.
        """
        self._workers = workers
        self._queue: asyncio.Queue[Task | None] | None = None
        self._handler: TaskHandler | None = None
        self._worker_tasks: list[asyncio.Task] = []
        self._running = False
        self._errors: list[TaskProcessingError] = []
        self._handlers: dict[type, TaskHandler] = {}

    def register_handler(self, task_type: type, handler: TaskHandler) -> None:
        """Registrate for task's handler"""
        if not isinstance(handler, TaskHandler):
            raise TypeError(
                f"{handler!r} doesn't release TaskHandler: wait for async def handle(task)"
            )
        self._handlers[task_type] = handler

    async def submit(self, task: Task) -> None:
        """Put task into queue"""
        if not self._running or self._queue is None:
            raise ExecutorNotStartedError()

        if self._handler is None and not hasattr(self, "_handlers"):
            raise ExecutorError("Handler not registered")

        await self._queue.put(task)

    async def wait_all(self) -> None:
        """wait for all tasks"""
        if self._queue:
            await self._queue.join()

    @property
    def errors(self) -> list[TaskProcessingError]:
        """Errors handler"""
        return list(self._errors)


    async def __aenter__(self) -> "AsyncTaskExecutor":
        """context manager"""
        self._queue = asyncio.Queue()
        self._running = True
        self._worker_tasks = [
            asyncio.create_task(self._worker_loop(f"worker-{i}"))
            for i in range(self._workers)
        ]
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Send sentinel for workers"""
        await self._queue.join()
        for _ in self._worker_tasks:
            await self._queue.put(None)         # send sentinel
        await asyncio.gather(*self._worker_tasks, return_exceptions=True)
        self._running = False
        return False

    async def _worker_loop(self, name: str) -> None:
        """worker's loop: take task from queue and handle it"""
        while True:
            task = await self._queue.get()
            if task is None:   # sentinel — выходим
                self._queue.task_done()
                break
            try:
                handler = None
                for task_type, h in self._handlers.items():
                    if isinstance(task, task_type):
                        handler = h
                        break
                if handler is None:
                    raise ExecutorError(f"No handler for task type {type(task)}")
                await handler.handle(task)

            except Exception as e:
                error = TaskProcessingError(task, e)
                self._errors.append(error)
                print(f"[{name}] error: {error}")
            finally:
                self._queue.task_done()