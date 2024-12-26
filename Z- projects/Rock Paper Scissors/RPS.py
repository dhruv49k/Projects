import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playerPick = input("Enter your choice :\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")
PChoice = int(playerPick)

if PChoice < 1 or PChoice > 3:
    sys.exit("Please enter valid choice")

compPick = random.choice("123")
CChoice = int(compPick)

print("")
print("Your choice is " + str(RPS(PChoice)).replace("RPS.", ""))
print("Python's choice is " + str(RPS(CChoice)).replace("RPS.", ""))
print("")

if PChoice == 1 | CChoice == 3:
    print("🎉 You win !!!")
elif PChoice == 2 | CChoice == 1:
    print("🎉 You win !!!")
elif PChoice == 3 | CChoice == 2:
    print("🎉 You win !!!")
elif PChoice == CChoice:
    print("😒 It's a draw !!!")
else:
    print("🐍 Python wins !!!")


# print(CChoice)
