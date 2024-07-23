import ToDoFunctions.ToDoFunctions as fn
import FreeSimpleGUI as gui

label = gui.Text("Type in a ToDo:")
inputBox = gui.InputText(tooltip="Enter ToDo", key="todo")
addButton = gui.Button("Add")

# Show Window
window = gui.Window("My ToDo App", 
                    layout=[[label], [inputBox,addButton]],
                    font=("Helvetica",10))
while True:
    event, values = window.read()
    if event == "Add":
        todos = fn.write_todos(values["todo"] + "\n", "a")
    elif event is None:
        break
window.close()