import asyncio
import pytest

from src.labwork_four.task_compleater import AsyncTaskExecutor


class TestTask:
    def __init__(self):
        self.processed = False


class TestHandler:
    async def handle(self, task):
        task.processed = True

class OrderTask:
    def __init__(self, name, log):
        self.name = name
        self.log = log


class SleepHandler:
    async def handle(self, task: OrderTask):
        task.log.append(f"{task.name}-start")

        if task.name == "A":
            # задача A "засыпает"
            await asyncio.sleep(0.1)

        task.log.append(f"{task.name}-end")



@pytest.mark.asyncio
async def test_task_processed():
    """Test for correct work task handler"""
    task = TestTask()

    async with AsyncTaskExecutor(workers=1) as executor:
        executor.register_handler(TestTask, TestHandler())
        await executor.submit(task)
        await executor.wait_all()

    assert task.processed is True

@pytest.mark.asyncio
async def test_async_switching():
    """Test for correct work async logic work"""
    log = []

    async with AsyncTaskExecutor(workers=2) as executor:
        executor.register_handler(OrderTask, SleepHandler())

        await executor.submit(OrderTask("A", log))
        await executor.submit(OrderTask("B", log))

        await executor.wait_all()

    assert log == [
        "A-start",
        "B-start",  # B выполняется, пока A "спит"
        "B-end",
        "A-end",
    ]

@pytest.mark.asyncio
async def test_submit_without_handler():
    """test for submit worker without handler"""
    executor = AsyncTaskExecutor()

    try:
        async with executor:
            await executor.submit(object())
    except Exception as e:
        assert e.__class__ == ValueError



@pytest.mark.asyncio
async def test_error_collection():
    """Error test"""
    class Task:
        def __init__(self):
            self.id = 1

    class FailingHandler:
        async def handle(self, task):
            raise ValueError("fail")

    async with AsyncTaskExecutor() as executor:
        executor.register_handler(Task, FailingHandler())
        await executor.submit(Task())
        await executor.wait_all()

        assert len(executor.errors) == 1