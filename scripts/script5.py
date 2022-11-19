while True:
    with open(r"C:\Users\omkarav\Downloads\python_learn\files\Heads_tails.txt", 'r') as file:
        sides = file.readlines()
    
    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open(r"C:\Users\omkarav\Downloads\python_learn\files\Heads_tails.txt", 'w') as file:
        file.writelines(sides)
    
    nr_heads = sides.count("head\n")

    print(nr_heads / len(sides) * 100)
    
