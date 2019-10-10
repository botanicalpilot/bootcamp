'''
make two versions:
    1. The user guesses computer's random number
        *Allow the user to make an unlimited number of guesses using a while loop
        *Tell user if guess is too high or low. Optional: tell user if last guess was closer or if current guess is closer
        *when finished ask to play again, quit, or switch with the computer (go to 2)
    
    2. The computer guesses the user input
        *make the bot make random guesses until correct. 
'''

import random

def lowHigh(userGuess, computerN):
    if userGuess > computerN:
        print('That guess is too high! Please try again.')
    else:
        print('That guess is too low! Please try again.')
    

def userGuess():
    print('Welcome to the Number Guessing Game. Try and guess the computers number in the range of 1-10. If incorrect, you will be prompted to guess again.' )
    computerN = random.randint(1,10)
    while True:
        userGuess = float(input("Guess a number: "))
        if userGuess == computerN:
            print(f'Your guess, {userGuess}, was correct!')
            break
        else:
            lowHigh(userGuess, computerN)

def storedGuess(prevGuess):
    prevGuess = None
    if prevGuess == None:
        break
    elif prevGuess 


userGuess()
