import os
from pathlib import Path

NAME = "files\\todos.txt"
def get_project_root(filename = NAME) -> Path:

    filepath = str(Path(__file__).parent.parent) + "\\" + filename
    if not os.path.exists(filepath):
        filepath = "..\\" + filename

    return filepath

if __name__ == "__main__":
    root = get_project_root() 
    print(root)