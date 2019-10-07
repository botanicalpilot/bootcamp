import random

def userRock(userRPC,botRPS):
    if userRPC != 'rock':
        return
    elif botRPS == 'rock':
        print("You both choose rock, it's a tie!")
    elif botRPS == 'paper':
        print("The computer used paper. Paper cover rock, you loose!")
    elif botRPS == 'scissors':
        print("The computer used scissors. Rock breaks scissors, you win!")
def userPaper(userRPC, botRPS):
    if userRPC != 'paper':
        return
    elif botRPS == 'rock':
        print("The computer used rock. Paper covers rock, you win!")
    elif botRPS == 'paper':
        print("You both choose paper, it's a tie")
    elif botRPS == 'scissors':
        print("The computer used scissors. Scissors cut paper, you loose!")
def userScissors(userRPC, botRPS):
    if userRPC != 'scissors':
        return
    elif botRPS == 'rock':
        print("The computer used rock. Rock breaks scissors, you loose!")
    elif botRPS == 'paper':
        print("The computer used paper. Scissors cut paper, you win!")
    elif botRPS == 'scissors':
        print("You both choose scissors, it's a tie!")       
def main():
    while True:
        "Welciome to the computerized Rock, Paper, Scissors Game!"
        userRPC = input("Type your choice, 'rock' 'paper', or 'scissors': ")
        choices = ['rock', 'paper', 'scissors']
        botRPS = random.choice(choices)
        userRock(userRPC, botRPS)
        userPaper(userRPC, botRPS)
        userScissors(userRPC, botRPS)
        again = input("Would you like to play again? Type 'Y for yes or 'N' for no. ")
        if again != 'Y':
            break

main()
