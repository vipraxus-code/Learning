from pathlib import Path

class TextFile:
    def __init__(self, path=Path("Python/Lessons/Task-69/text.txt")):
        self.path = path

    def show(self):
        print(self.path.read_text().strip())

    def write(self, content):
        self.path.write_text(f"{self.path.read_text()}{content}\n")

    def clear(self):
        self.path.write_text("")