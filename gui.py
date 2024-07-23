import ToDoFunctions.ToDoFunctions as fn
import FreeSimpleGUI as gui

label = gui.Text("Type in a ToDo:")
inputBox = gui.InputText(tooltip="Enter ToDo")
addButton = gui.Button("Add")

# Show Window
window = gui.Window("My ToDo App", layout=[[label], [inputBox,addButton]])
window.read()
window.close()