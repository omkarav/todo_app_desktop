date=input("enter todays date:")
mood=input('what is your mood today from 1 to 10?')
thoughts=input("let your thoughts flow:\n")
with open(fr"C:\Users\omkarav\Downloads\python_learn\files\{date}",'w') as file:
    file.writelines(f"todays mood rating is {mood} " + 2 * "\n")
    file.writelines(thoughts)    