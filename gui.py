import ToDoFunctions.ToDoFunctions as fn
import FreeSimpleGUI as gui
import time

gui.theme("BrownBlue")

clockLabel = gui.Text("",key = "Clock")
label = gui.Text("Type in a ToDo:")
inputBox = gui.InputText(tooltip="Enter ToDo", key="ToDo")
addButton = gui.Button("Add")
listBox = gui.Listbox(values=fn.get_todos(), 
                      key="ToDoList", enable_events=True,
                      size=[45,10])
editButton = gui.Button("Edit")
completeButton = gui.Button("Complete")
exitButton = gui.Button("Exit")

# Show Window
window = gui.Window("My ToDo App", 
                    layout=[[clockLabel],
                            [label], 
                            [inputBox,addButton],
                            [listBox, editButton, completeButton],
                            [exitButton]],
                    font=("Helvetica",10)) 
while True:
    event, values = window.read(timeout=1000)
    if event is None:
        break
    window["Clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))

    if event == "Add":
        if values["ToDo"] != "":
            # Get ToDo List
            todos = fn.get_todos()
            # Add new element to ToDo List
            todos.append(values["ToDo"].title() + "\n")
            # Add new ToDo to file
            fn.write_todos(todos)
            # Add new ToDo to GUI
            window["ToDoList"].update(values=todos)
        else:
            gui.popup("Please write a ToDo first",
                      font=("Helvetica",10))
            
    elif event == "ToDoList":
        window["ToDo"].update(value = values["ToDoList"][0].strip())

    elif event == "Edit":
        try:
            #
            toDoToEdit = values["ToDoList"][0]
            newToDo = values["ToDo"].title() + "\n"
            # Get an update ToDo List
            todos = fn.get_todos()
            index = todos.index(toDoToEdit)
            todos[index] = newToDo
            # Updte ToDo List file
            fn.write_todos(todos)
            # Updte ToDo List GUI
            window["ToDoList"].update(values=todos)
        except IndexError:
            gui.popup("Please select an item first",
                      font=("Helvetica",10))

    elif event == "Complete":
        try:
            todoToComplete = values["ToDoList"][0]
            # Get ToDo
            todos = fn.get_todos()
            # Delete Todo
            todos.pop(todoToComplete)
            # Updade ToDo List file
            fn.write_todos(todos)
            # Updade ToDo List GUI
            window["ToDoList"].update(values=todos)
            # Update ToDo Inputbox
            window["ToDo"].update(value = "")
        except IndexError:
            gui.popup("Please select an item first",
                      font=("Helvetica",10))
    
    elif (event == "Exit"):
        break
window.close()