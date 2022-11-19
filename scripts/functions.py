def get_todos(filepath="data.txt"): # we are using default parameter , if nothing is passed this value is taken by default 
    with open(filepath,'r') as file: # this is using with context instead of open() for files , advantage is here with automatically closes the file even though there is some error and , but in open(), only if code reaches the close() line then only file gets closed.
            todos=file.readlines()
    return todos

def write_todos(todos_arg,filepath="data.txt"):
    with open(filepath,'w') as file:
            file.writelines(todos_arg)

print ("i am outside if")

print (__name__)

if __name__ == "__main__":   # this is used to execute the below lins only when this file is executed explicitly , not when called 
                             #  by some other file.
    print (" i am inside if ")
    print (get_todos())
