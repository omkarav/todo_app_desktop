#from functions import get_todos,write_todos 
""" we can use this method of calling functions or below line method 
if we use this method , then no need to mention "functions." as we are already calling all the functions before hand.
 """
import functions
# if we have different folder then we can use 
# from <folername> import functions

while True:
    user_action=input("enter show or add/new or edit or complete or exit: ")
    user_action=user_action.strip() # to strip the space characters from the input string 
   
    if user_action.startswith("add"):
      
      #  todo=user_action.strip("add ")
        # or 
        todo=user_action[4:] # this will extract all characters from string starting from index 4
        
      
        todos=functions.get_todos()
        todos.append(todo + "\n" )
        
        functions.write_todos(todos_arg=todos)

    elif user_action.startswith("show"):
        
        todos=functions.get_todos()
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
            todos=functions.get_todos()

            new_todo=input("enter the new todo: ")
            todos[number]=new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("enter the line number to edit")
    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])
            todos=functions.get_todos()
            todos.pop(number -1)
            functions.write_todos(todos)
            print (todos)
        except ValueError:
            print("enter the line number to edit")
        except IndexError:
            print(" please enter the number in the range ")
    elif user_action.startswith("exit"):
        break
    else:
        print ("enter proper command")
        