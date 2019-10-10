'''
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance

Things to remember:
order matters, matching several numbers means matching them in a row. 

'''
import random 


def pick6():
    for n in range(6):
        winningTicket.append(random.choice(range(1,99)))
    print(winningTicket)

def tryingTheLottery(winningTicket):
    for n in range(100000):
        for n in range(6):
            userTicket = random.choice(range(1,99))
        if userTicket != winningTicket:
            cost.append(2)
            #print("try again")
        else:
            partialMatch(winningTicket, userTicket)
            cost.append(2)
            print("Your ticket is the winning ticket!")
    

def partialMatch(winningTicket, userTicket):
    if winningTicket[0] in userTicket[0]:
        print("you matched the first number")
        winnings.append(4)
    elif winningTicket[0:1] in userTicket[0:1]:
        print("you matched the first two numbers")
        winnings.append(7)
    elif winningTicket[0:2] in userTicket[0:2]:
        print("you matched the first three numbers")
        winnings.append(100)
    elif winningTicket[0:1] in userTicket[0:3]:
        print("you matched the first four numbers")
        winnings.append(50000)
    elif winningTicket[0:4] in userTicket[0:4]:
        print("you matched the first five numbers")
        winnings.append(1000000)
    elif winningTicket[0:5] in userTicket[0:5]:
        print("You won the lotto!")
        winnings.append(25000000)
    else:
        return


def totalCost(cost):
    total = 0
    for n in cost:
        total += n
    return total
def totalWinnings(winnings):
    winningsEarned = 0
    for n in winnings:
        winningsEarned += n
    return winningsEarned

cost = []
winningTicket = []
winnings = []
userTicket = []
pick6()
tryingTheLottery(winningTicket)
print(totalCost(cost))
print(totalWinnings(winnings))