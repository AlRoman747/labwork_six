from check_source import *

def main():
    sources = [
        RandomTaskGenerate,
        ReadFromFile,
        APISimulate
    ]

    Reader = ReadFromFile()
    print(Reader.get_tasks())

    for source in sources:
        print(check_source(source()))


if __name__ == "__main__":
    main()