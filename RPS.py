import random


userRPC = input("Type your choice, 'rock' 'paper', or 'scissors': ")
choices = ['rock', 'paper', 'scissors']
botRPS = random.choice(choices)

def userRock():
    if userRPC != 'rock':
        return
    elif botRPS == 'rock':
        print("You both choose rock, it's a tie!")
    elif botRPS == 'paper':
        print("The computer used paper. Paper cover rock, you loose!")
    elif botRPS == 'Scissors':
        print("The computer used scissors. Rock breaks scissors, you win!")
    return
def userPaper():
    if userRPC != 'paper':
        return
    elif botRPS == 'rock':
        print("The computer used rock. Paper covers rock, you win!")
    elif botRPS == 'paper':
        print("You both choose paper, it's a tie")
    elif botRPS == 'Scissors':
        print("The computer used scissors. Scissors cut paper, you loose!")
    return
def userScissors():
    if userRPC != 'paper':
        return
    elif botRPS == 'rock':
        print("The computer used rock. Rock breaks scissors, you loose!")
    elif botRPS == 'paper':
        print("The computer used paper. Scissors cut paper, you win!")
    elif botRPS == 'Scissors':
        print("You both choose scissors, it's a tie!")
    return


def main():
    "Welciome to the computerized Rock, Paper, Scissors Game!"
    userRock()
    userPaper()
    userScissors()

main()
