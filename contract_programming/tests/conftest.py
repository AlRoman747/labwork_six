import pytest

from contract_programming.src import APISimulate
from contract_programming.src import RandomTaskGenerate

@pytest.fixture
def api():
    return APISimulate()


@pytest.fixture
def generator():
    return RandomTaskGenerate()
