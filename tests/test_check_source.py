import pytest
from src.check_source import SourceChecker
from src.random_source import RandomTaskGenerate
from src.file_source import ReadFromFile
from src.api_source import APISimulate

class BadTestClass:
    def func(self):
        pass

@pytest.mark.parametrize(
    "source_class",
    [RandomTaskGenerate, APISimulate]
)
def test_check_source_valid(source_class):
    checker = SourceChecker(source_class())
    result = checker.check_source()

    assert result == f"{source_class.__name__}: Контракт соблюдён"
@pytest.mark.parametrize(
    "bad_class",
    [BadTestClass]
)
def test_check_source_invalid(bad_class):
    checker = SourceChecker(bad_class())

    with pytest.raises(TypeError):
        checker.check_source()