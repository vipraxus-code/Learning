from pathlib import Path


def count_words(file_name, word):
    path = Path(file_name)
    try:
        print(f"The string '{word}' appears {path.read_text(encoding='utf-8').lower().count(word.lower())} times.")
    except FileNotFoundError:
        print("There is no such file.")