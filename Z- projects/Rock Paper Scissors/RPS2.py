# Rock Paper Scissors using everything learned
import sys
import random
from enum import Enum

def rps():

    game_count=0
    playerWin=0
    pythonWin=0

    def continuePlay():

        playagain = input("\nWant to Continue playing?\nY for yes\nN for no\n")

        if playagain.lower() == "y":
            print("\nOk\n")
            playRPS()

        elif playagain.lower() == "n":
            print("\n🙌🙌🙌🙌")
            print("\nThank you for playing")
            sys.exit("\n🙌Have a Great Day!!!🙌")

        else:
            print("\nInvalid input!!!\nEnter valid choice!!!\n")
            continuePlay()

    def playRPS():
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerPick = input("Enter your choice :\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")
        PChoice = int(playerPick)

        if (playerPick not in ["1","2","3"]):
            print("\nInvalid Choice!!!")
            playRPS()

        compPick = random.choice("123")
        CChoice = int(compPick)

        print(f"\nYour choice is {str(RPS(PChoice)).replace("RPS.", "")}.")
        print(f"Python's choice is {str(RPS(CChoice)).replace("RPS.", "")}.\n")

        def game_decision(PChoice, CChoice):
            
            nonlocal playerWin
            nonlocal pythonWin

            if PChoice == 1 | CChoice == 3:
                playerWin += 1
                return "🎉 You win !!!"
            elif PChoice == 2 | CChoice == 1:
                playerWin += 1
                return "🎉 You win !!!"
            elif PChoice == 3 | CChoice == 2:
                playerWin += 1
                return "🎉 You win !!!"
            elif PChoice == CChoice:
                return "😒 It's a draw !!!"
            else:
                pythonWin += 1
                return "🐍 Python wins !!!"
        
        game_result = game_decision(PChoice,CChoice)
        print(game_result)

        nonlocal game_count
        game_count+=1

        print(f"\nGame Count: {game_count}")
        print(f"Player Win: {playerWin}")
        print(f"Python Win: {pythonWin}")

        continuePlay()
    
    return playRPS

game=rps()

if __name__ =="__main__":
    game()

