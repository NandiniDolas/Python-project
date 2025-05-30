import random
'''
1 = rock
0 = paper
-1 = scissor


'''

computer = random.choice([1, 0, -1])
youstr = input("Enter your choice: ")
udict = {"r": 1,"p": 0, "s": -1}
reversedict = {1: "rock", 0: "paper", -1: "scissor"}

u = udict[youstr]

print(f"you choose {reversedict[u]}\nComputer choose {reversedict[computer]}")

if (computer == u):
    print("draw")

else:
    if(computer == 0 and u == 1):
        print("You lose")

    if(computer == 1 and u == 0):
        print("you win")

    if(computer == -1 and u == 1):
        print("You lose")

    if(computer == 1 and u == -1):
        print("You win")

    if(computer == 0 and u == -1):
        print("You win")

    if(computer == -1 and u == 0):
        print("You lose")

    else:
        print("Something went wrong")

# feedback = input("Please share your feedback: ")