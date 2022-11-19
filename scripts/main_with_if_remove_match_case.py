
while True:
    user_action=input("enter show or add/new or edit or complete or exit: ")
    user_action=user_action.strip() # to strip the space characters from the input string 
   
    if 'add' in user_action or 'new' in user_action:
      
        todo=user_action.strip("add ")
        # or 
        todo=user_action[4:] # this will extract all characters from string starting from index 4
        
        with open('data.txt','r') as file: # this is using with context instead of open() for files , advantage is here with automatically closes the file even though there is some error and , but in open(), only if code reaches the close() line then only file gets closed.
            todos=file.readlines()
        todos.append(todo + "\n" )
        
        with open('data.txt','w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        
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
    elif 'edit' in user_action:
        number=int(input("enter the number for todo to edit: ")) # output of input function is always a string , so adding int to make it number
        number=number -1
        with open('data.txt','r') as file:
            todos=file.readlines()

        new_todo=input("enter the new todo: ")
        todos[number]=new_todo + "\n"
        with open('data.txt','w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number=int(input("enter the number for item to be removed: "))
        with open('data.txt','r') as file:
            todos=file.readlines()
        todos.pop(number -1)
        with open('data.txt','w') as file:
            file.writelines(todos)
        print (todos)
    elif 'exit' in user_action:
        break
    else:
        print ("enter proper command")
        