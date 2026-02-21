from pathlib import Path

file = Path("Python/Lessons/Task-68/text.txt")
print(file.read_text().replace("Python", "C"))
