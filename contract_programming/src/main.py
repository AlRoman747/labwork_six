from check_source import SourceChecker
from random_source import RandomTaskGenerate
from file_source import ReadFromFile
from api_source import APISimulate


def main():
    sources = [
        RandomTaskGenerate,
        ReadFromFile,
        APISimulate
    ]


    for source in sources:
        checker = SourceChecker(source())
        print(checker.check_source())


if __name__ == "__main__":
    main()