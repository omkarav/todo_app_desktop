password=input("enter the password: ")
result={}
if len(password) >=8:
     result["length"]=True
else:
     result["length"]=False
digit=False
for i in password:
    if i.isdigit():
        digit=True
result["digits"]=digit
upper=False
for i in password:
    if i.isupper():
        upper=True
result["uppercase"]=upper

print(result)
print (all(result.values()))
if all(result.values()):
#if result.count(False) =0: we can also use this 
    print("Strong password")
else:
    print("weak password")
