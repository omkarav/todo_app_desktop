import functions
import PySimpleGUI as sg
import os

for filename in ["data.txt","item_status.txt","completed.txt"]:
    if not os.path.exists(filename):
        with open(filename,'w') as file:
            pass

sg.theme('Kayak')

label=sg.Text("Type in a to-do")
label0=sg.Text("Todo - list ",size=46)
label1=sg.Text("Status ")
label2=sg.Text("Completed Item list - last 5 items ")
input_box=sg.InputText(tooltip="enter to-do",key="todo")
add_button=sg.Button("add",mouseover_colors="LightBlue2")
list_items=sg.Listbox(values=functions.get_todos(),key="todos_item",enable_events=True,size=[45,10])
completed_items=sg.Listbox(values=functions.get_todos(filepath="completed.txt"),key="todos_completed",size=[60,5])
edit_button=sg.Button("edit")
complete_button=sg.Button("complete")
list_list=functions.get_todos()
count_list=len(list_list)
combo_list=sg.Combo(['start','started','in-progress', 'completed'],default_value='start',readonly=True,key="combo",enable_events=True)
#status_items=sg.InputCombo([combo_list1,combo_list2], size=(15, 10)),
#status_list = [" " for i in range(0,count_list)]
#print (list_list)
#print (status_list)
status_items=sg.Listbox(values=functions.get_todos(filepath="item_status.txt"),key="todos_status",enable_events=True,size=[13,10])
window=sg.Window("My TO-DO APP",layout=[[label,input_box,add_button,combo_list],[label0,label1],[list_items,status_items,edit_button,complete_button],[label2],[completed_items]], font=('Helevatica',15))
while True:
    event,value=window.read()
    print(event)
    print(value)
    match event:
        case "add":
           if value["todo"] == " " or value["todo"] == "":
             sg.popup("Please add some text to add ",font=('Helevatica',15))
           else:
            todos=functions.get_todos()
            new_todo=value["todo"] + "\n"
            todos.append(new_todo)
            todos_status=functions.get_todos(filepath="item_status.txt")
            todos_status.append(f"start \n")
            functions.write_todos(todos)
            functions.write_todos(todos_status,filepath="item_status.txt")
            window["todos_item"].update(values=todos)
            window["todos_status"].update(values=todos_status)
        case sg.WIN_CLOSED:
            break
        case "todos_item":
            try:
                window['todo'].update(value=value["todos_item"][0])
            except IndexError:
                pass
        case "edit":
            try:
                todos=functions.get_todos()
                todo_to_edit=value["todos_item"][0]
                print (todo_to_edit)
                index=todos.index(todo_to_edit)
                todos[index]=value["todo"].replace("\n","") + "\n"
                functions.write_todos(todos)
                window["todos_item"].update(values=todos)
            except IndexError:
                ex1=sg.Text("Please click on the To-DO list to edit (or) empty TO-DO list is selected to edit")
                ex2=sg.Button("OK",pad=(350,0),enable_events=True)
                window1=sg.Window("Please check this",layout=[[ex1],[ex2]], font=('Helevatica',15))
                event1,value=window1.read()
                match event1:
                    case "OK":
                        window1.close()

        case "complete":
            try:
                todos=functions.get_todos()
                todos_status=functions.get_todos(filepath="item_status.txt")
                todos_completed=functions.get_todos(filepath="completed.txt")
                todo_to_edit=value["todos_item"][0] 
                index=todos.index(todo_to_edit)
                if len(todos_completed) == 5:
                    todos_completed.pop(4)
                functions.write_todos(todos_completed,filepath="completed.txt")
                todos_completed.insert(0,todo_to_edit)
                todos.pop(index)
                todos_status.pop(index)
                functions.write_todos(todos)
                functions.write_todos(todos_status,filepath="item_status.txt")
                functions.write_todos(todos_completed,filepath="completed.txt")
                window["todos_item"].update(values=todos)
                window["todos_status"].update(values=todos_status)
                window["todos_completed"].update(values=todos_completed)
            except IndexError:
                ex1=sg.Text("Please click on the To-DO list to complete (or) empty TO-DO list is selected to complete")
                ex2=sg.Button("OK",pad=(350,0),enable_events=True)
                window1=sg.Window("Please check this",layout=[[ex1],[ex2]], font=('Helevatica',15))
                event1,value=window1.read()
                match event1:
                    case "OK":
                        window1.close()

                
        case "combo":
            try:
                todos=functions.get_todos()
                print (todos)
                ix1=todos.index(value["todos_item"][0])
                todos_new=functions.get_todos(filepath="item_status.txt")
                todos_new[ix1]=value["combo"] + "\n"
                functions.write_todos(todos_new,filepath="item_status.txt")
                window["todos_status"].update(values=todos_new)
            except IndexError:
                sg.popup("Please click on the To-DO list to change progress ",font=('Helevatica',15))
                
                
                


window.close()






