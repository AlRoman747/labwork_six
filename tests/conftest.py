import pytest

from src import APISimulate
from src import RandomTaskGenerate

@pytest.fixture
def api():
    return APISimulate()


@pytest.fixture
def generator():
    return RandomTaskGenerate()
