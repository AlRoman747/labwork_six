from check_source import check_source
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
        print(check_source(source()))


if __name__ == "__main__":
    main()