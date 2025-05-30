import random

'''
-1 is water
1 is snake
0 is gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict ={"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"you choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("its draw")

else: 
    if(computer == -1 and you == 1):
        print("You win")
    
    if(computer == -1 and you == 0):
        print("You Lose")

    if(computer == 1 and you == -1):
        print("You lose")

    if(computer == 1 and you == 0):
        print("You win")

    if(computer == 0 and you == -1):
        print("You win")

    if(computer == 0 and you == 1):
        print("You lose")

    else:
        print("Something went wrong")
