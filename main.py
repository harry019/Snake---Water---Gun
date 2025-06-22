'''
SNAKE WATER GUN 
'''
import random

print("🎮 Welcome to SNAKE 🐍 WATER 💧 GUN 🔫 Game!")
print("Type S for Snake, W for Water, G for Gun or type 'exit' to quit.")

youDict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

def main():
    while True:
        youstr = input("\nYour choice (S/W/G or exit): ").strip().upper()

        if youstr == "EXIT":
            print("👋 Thanks for playing! Goodbye!")
            break

        if youstr not in youDict:
            print("❌ Invalid input! Please enter S, W, or G.")
            continue

        computer = random.choice([-1, 0, 1])
        you = youDict[youstr]

        print(f"You chose {reverseDict[you]}")
        print(f"Computer chose {reverseDict[computer]}")

        if computer == you:
            print("🤝 It's a Draw!")
        elif (you == 1 and computer == -1) or \
             (you == -1 and computer == 0) or \
             (you == 0 and computer == 1):
            print("✅ You Win!")
        else:
            print("❌ You Lose!")

if __name__ == "__main__":
    main()
