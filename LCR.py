'''
LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves. Description from wikipedia:

Each player receives at least 3 chips. Players take it in turn to roll three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to his left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.
If a player has fewer than three chips left, he/she is still in the game but his number of chips is the number of dice he/she rolls on his/her turn, rather than rolling all three. When a player has zero chips, he/she passes the dice on his turn, but may receive chips from others and take his next turn accordingly. The winner is the last player with chips left. He/she does not roll the dice, and wins the center pot. If he/she chooses to play another round, he/she does not roll 3, he/she keeps his pot and plays with that.
When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again.

Strategy:
    -build a function for the 6-sided dice marked with "L", "C", "R", and 'dot' on the remaining sides
    -each player needs to 'roll' the dice, depending on what side is selected the chips will be exchanged.
    -when only one player has chips left, break while loop using the function(s) and ask if they want to play again.


'''
import random
import time

playernames = input("Enter the names of three players, seperated by spaces ")
players = playernames.split()
player1 = [players[0], 3]
player2 = [players[1], 3]
player3 = [players[2], 3]
pot = int(0)

def roll(x):
    if x > 0:
        dice = ['L', 'C', 'R', 'dot', 'dot', 'dot']
        print("rolling the dice")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        diceresult = [random.choice(dice), random.choice(dice), random.choice(dice)]
        print(f"You rolled {diceresult[0]}, {diceresult[1]}, and {diceresult[2]}")
        numberdots = diceresult.count('dot')
        numberL = diceresult.count('L')
        numberC = diceresult.count('C')
        numberR = diceresult.count('R')
    if numberL > 0:
        player1[1] -= numberL
        print(player1[1])

roll(4)
