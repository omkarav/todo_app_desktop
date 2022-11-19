numbers=[10.3,334.55,43.33] # need to remove quotes to remove the string functionality 
numbers=[int(item) for item in numbers]
print(numbers)