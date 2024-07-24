import ToDoFunctions.ToDoFunctions as fn
import FreeSimpleGUI as gui

label = gui.Text("Type in a ToDo:")
inputBox = gui.InputText(tooltip="Enter ToDo", key="toDo")
addButton = gui.Button("Add")
listBox = gui.Listbox(values=fn.get_todos(), 
                      key="toDoList", enable_events=True,
                      size=[45,10])
editButton = gui.Button("Edit")

# Show Window
window = gui.Window("My ToDo App", 
                    layout=[[label], 
                            [inputBox,addButton],
                            [listBox, editButton]],
                    font=("Helvetica",10)) 
while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        # Get ToDo List
        toDos = fn.get_todos()
        # Add new element to ToDo List
        toDos.append(values["toDo"].title() + "\n")
        # Add new ToDo to file
        fn.write_todos(toDos)
        # Add new ToDo to GUI
        window["toDoList"].update(values=toDos)
    elif event == "toDoList":
        window["toDo"].update(value = values["toDoList"][0])

    elif event == "Edit":
        #
        toDoToEdit = values["toDoList"][0]
        newToDo = values["toDo"].title() + "\n"
        # Get an update ToDo List
        toDos = fn.get_todos()
        index = toDos.index(toDoToEdit)
        toDos[index] = newToDo
        # Updte ToDo List file
        fn.write_todos(toDos)
        # Updte ToDo List GUI
        window["toDoList"].update(values=toDos)

    elif event is None:
        break
window.close()