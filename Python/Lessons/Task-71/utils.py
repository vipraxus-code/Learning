from pathlib import Path

def print_names(file_name):
    path = Path(file_name)
    try:
        content = path.read_text().splitlines()
        for name in content:
            print(name)
    except FileNotFoundError:
        print("There is no such file.")    
