
while True:
    user_action=input("enter show or add or edit or exit: ")
    user_action=user_action.strip() # to strip the space characters from the input string 
    match user_action:
        case "add":
            todo=input('enter the todo: ') + "\n"
            file=open('data.txt','r')
            todos=file.readlines()
            file.close()
            todos.append(todo)
            file=open('data.txt','w')
            file.writelines(todos)
            file.close()
        case "show":
            file=open('data.txt','r')
            todos=file.readlines()
            file.close()
            print(todos)
         #   new_todos=[]    we have 2 ways to trim one  \n lines , ( we will get 2)one is from list values from file , other is from print 
        ##    for item in todos:
         #       new_item=item.strip("\n")
         #       new_todos.append(new_item)
         #   new_todos=[item.strip("\n") for item in todos] # second method , list comprehension 
            for index,item in enumerate(todos):
             item=item.strip("\n") # third method to get rid of second new line in the output 
             row=f"{index +1}.{item}"   
             print(row) 
        case "edit":
            number=int(input("enter the number for todo to edit: ")) # output of input function is always a string , so adding int to make it number
            number=number -1
            new_todo=input("enter the new todo: ")
            todos[number]=new_todo
        case "complete":
            number=int(input("enter the number for item to be removed: "))
            todos.pop(number -1)
            print (todos)
        case "exit":
            break
        case _:
            print(" please enter proper input")