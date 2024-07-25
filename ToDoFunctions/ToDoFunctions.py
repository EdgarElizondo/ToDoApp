from src.utils import get_project_root

# Read Function
def get_todos(filepath = get_project_root()):
    with open(filepath,"r") as f:
        todos = f.readlines()
    return todos

# Write Function
def write_todos(file, type_writing = "w", filepath = get_project_root()):
    with open(filepath, type_writing) as f:
        f.writelines(file)