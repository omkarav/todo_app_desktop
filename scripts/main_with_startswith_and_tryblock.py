
while True:
    user_action=input("enter show or add/new or edit or complete or exit: ")
    user_action=user_action.strip() # to strip the space characters from the input string 
   
    if user_action.startswith("add"):
      
        todo=user_action.strip("add ")
        # or 
        todo=user_action[4:] # this will extract all characters from string starting from index 4
        
        with open('data.txt','r') as file: # this is using with context instead of open() for files , advantage is here with automatically closes the file even though there is some error and , but in open(), only if code reaches the close() line then only file gets closed.
            todos=file.readlines()
        todos.append(todo + "\n" )
        
        with open('data.txt','w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        
        with open('data.txt','r') as file:
            todos=file.readlines()
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
    elif user_action.startswith("edit"):
        try:
            number= int(user_action[5:]) # taking the new todo woth same line as entering edit
            number=number -1
            with open('data.txt','r') as file:
                todos=file.readlines()

            new_todo=input("enter the new todo: ")
            todos[number]=new_todo + "\n"
            with open('data.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print("enter the line number to edit")
    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])
            with open('data.txt','r') as file:
                todos=file.readlines()
            todos.pop(number -1)
            with open('data.txt','w') as file:
                file.writelines(todos)
            print (todos)
        except ValueError:
            print("enter the line number to edit")
        except IndexError:
            print(" please enter the number in the range ")
    elif user_action.startswith("exit"):
        break
    else:
        print ("enter proper command")
        