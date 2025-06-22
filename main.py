'''
SNAKE WATER GUN 
'''
import random
print("SNAKE WATER GUN")
youDict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

computer = random.choice([-1, 0, 1])

youstr = input("S for snake🐍, W for water💧, G for gun🔫: ").strip().upper()

if youstr not in youDict:
    print("Invalid input! Please enter S, W, or G.")
else:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a Draw!")
    elif (you == 1 and computer == -1) or \
         (you == -1 and computer == 0) or \
         (you == 0 and computer == 1):
        print("You Win!")
    else:
        print("You Lose!")