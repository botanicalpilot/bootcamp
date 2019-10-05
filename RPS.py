import random

def get_variables():
    userRPC = input("Type your choice, 'rock' 'paper', or 'scissors': ")
    choices = ['rock', 'paper', 'scissors']
    botRPS = random.choice(choices)
def userRock():
    if userRPC != 'rock'
        break
    elif:
        if botRPS == 'rock'
        print("You both choose rock, it's a tie!")
    elif:
        if botRPS == 'paper'
        print("The computer used paper. Paper cover rock, you loose!")
    else:
        print("The computer used scissors. Rock breaks scissors, you win!")
def userPaper():
    if userRPC != 'paper'
        break
    elif:
        if botRPS == 'rock'
        print("The computer used rock. Paper covers rock, you win!")
    elif:
        if botRPS == 'paper'
        print("You both choose paper, it's a tie")
    else:
        print("The computer used scissors. Scissors cut paper, you loose!")
def userScissors():
    if userRPC != 'scissors'
        break
    elif:
        if botRPS == 'rock'
        print("The computer used rock. Rock breaks scissors, you loose!")
    elif:
        if botRPS == 'paper'
        print("The computer used paper. Scissors cut paper, you win!")
    else:
        print("You both choose scissors, it's a tie!")


def main():
    "Welciome to the computerized Rock, Paper, Scissors Game!"
    get_variables()
    userRock()
    userPaper()
    userScissors()

main()
