FILEPATH = "files/todos.txt"

# Read Function
def get_todos(filepath = FILEPATH):
    with open(filepath,"r") as f:
        todos = f.readlines()
    return todos

# Write Function
def write_todos(file, type_writing = "w", filepath = FILEPATH):
    with open(filepath, type_writing) as f:
        f.writelines(file)