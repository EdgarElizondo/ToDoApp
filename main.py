import time
from ToDoFunctions.ToDoFunctions import get_todos, write_todos

prompt = "Enter a ToDo: "

time_now = time.strftime("%b %d, %Y %H:%M")
print(time_now)

while True:
    todo_activity = input("Type add, show edit, complete or exit: ").lower().strip()
    
    if todo_activity.startswith("add"):
        # Get Number activity
        if len(todo_activity) > 3:
            todo = todo_activity[4:]
        else:
            todo = input(prompt)
        # Read the ToDo file
        write_todos(todo + "\n","a")
        
    elif todo_activity.startswith("show"):
        # Read the ToDo file
        todos = get_todos()
        # Print the ToDo file
        for i, todo in enumerate(todos):
            print(f"{i+1}.- {todo.capitalize()}",end="")
            
    elif todo_activity.startswith("edit"):
        # Get Number activity
        if len(todo_activity) > 4:
            try:
                num_activity = int(todo_activity[5:])
            except ValueError:
                print("Wrong instruction, please insert the number activity insetead the activity itself.")
                continue
        else:
            num_activity = int(input("Insert the number activity which you want to edit: "))
        # Read the ToDo file
        todos = get_todos()
        # In case the number is out of limits
        if num_activity > len(todos):
            print(f"The index is out of limits, please select and index between the range 1 to {len(todos)}")
            continue
        # Edit changes
        new_activity = input(prompt)
        todos[num_activity - 1] = new_activity + "\n"
        # Save changes
        write_todos(todos)
    
    elif todo_activity.startswith("complete"):
        # Get Number activity
        if len(todo_activity) > 8:
            number = int(todo_activity[9:])
        else:
            try:
                number = int(input("Number of the activity which was completed: "))
            except ValueError:
                print("Wrong instruction, please insert the number activity insetead the activity itself.")
                continue
        # Read the ToDo file
        todos = get_todos()
        # In case the number is out of limits
        if number > len(todos):
            print(f"The index is out of limits, please select and index between the range 1 to {len(todos)}")
            continue
        # Remove ToDo activity
        todo_to_remove = todos.pop(number - 1)
        # Save changes
        write_todos(todos)
        # Notification that the ToDo was removed succesfully
        print(f"ToDo '{todo_to_remove.strip()}' was removed from the list")
                
    elif todo_activity.startswith("exit"):
        break

    else:
        print("Wrong instruction")