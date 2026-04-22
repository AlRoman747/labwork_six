import asyncio

from src.labwork_four.HandlerProtocol import TaskHandler
from src.labwork_four.errors_handlers import TaskProcessingError, ExecutorNotStartedError, ExecutorError
from src.labwork_two.find_source_tasks import Task


class AsyncTaskExecutor:
    """Асинхронный исполнитель задач.

    Поддерживает несколько конкурентных workers.
    Управляется через контекстный менеджер:

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

    def register_handler(self, handler: object) -> None:
        """Зарегистрировать обработчик задач.

        Raises:
            TypeError: Если handler не реализует TaskHandler.
        """
        if not isinstance(handler, TaskHandler):
            raise TypeError(
                f"{handler!r} не реализует TaskHandler: ожидается async def handle(task)"
            )
        self._handler = handler

    async def submit(self, task: Task) -> None:
        """Поставить задачу в очередь.

        Raises:
            ExecutorNotStartedError: Если исполнитель не запущен.
        """
        if not self._running or self._queue is None:
            raise ExecutorNotStartedError(
                "Исполнитель не запущен. Используйте 'async with'"
            )
        await self._queue.put(task)

    async def wait_all(self) -> None:
        """Подождать обработки всех задач в очереди."""
        if self._queue:
            await self._queue.join()

    @property
    def errors(self) -> list[TaskProcessingError]:
        """Ошибки, возникшие при обработке задач."""
        return list(self._errors)

    # ── контекстный менеджер ──

    async def __aenter__(self) -> "AsyncTaskExecutor":
        self._queue = asyncio.Queue()
        self._running = True
        self._worker_tasks = [
            asyncio.create_task(self._worker_loop(f"worker-{i}"))
            for i in range(self._workers)
        ]
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> bool:
        # Отправляем sentinel для каждого worker'а
        for _ in self._worker_tasks:
            await self._queue.put(None)
        # Ждём завершения всех workers
        await asyncio.gather(*self._worker_tasks, return_exceptions=True)
        self._running = False
        return False

    # ── внутренний worker ──

    async def _worker_loop(self, name: str) -> None:
        """Цикл worker'а: берёт задачи из очереди и обрабатывает."""
        while True:
            task = await self._queue.get()
            if task is None:   # sentinel — выходим
                self._queue.task_done()
                break
            try:
                if self._handler is None:
                    raise ExecutorError("Обработчик не зарегистрирован")
                await self._handler.handle(task)
            except Exception as e:
                error = TaskProcessingError(task, e)
                self._errors.append(error)
                print(f"[{name}] ОШИБКА: {error}")
            finally:
                self._queue.task_done()