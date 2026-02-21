from pathlib import Path

file = Path("Python/Lessons/Task-67/text.txt")
for line in file.read_text().splitlines():
    print(line)