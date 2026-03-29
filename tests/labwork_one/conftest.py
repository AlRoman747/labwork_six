import pytest

from src.labwork_one.api_source import APISimulate
from src.labwork_one.random_source import RandomTaskGenerate

@pytest.fixture
def api():
    return APISimulate()


@pytest.fixture
def generator():
    return RandomTaskGenerate()
