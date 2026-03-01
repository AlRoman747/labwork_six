import pytest
from src.api_source import APISimulate
from src.random_source import RandomTaskGenerate


@pytest.fixture
def api():
    return APISimulate()


@pytest.fixture
def generator():
    return RandomTaskGenerate()
