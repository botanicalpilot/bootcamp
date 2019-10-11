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

cost = []

winnings = []
userTicket = []

def pick6():
    winningTicket = []
    for n in range(6):
        winningTicket.append(random.choice(range(1,99)))
    return winningTicket

def testingLotteryTicket():
    #print(f'winning ticket:{winningTicket}')
    for n in range(100):
        #userTicket = []
        cost.append(2)
def makeLotteryTicket():
    tempTicket = []
    for n in range(6):
        tempTicket.append(random.choice(range(1,99)))  
        userTicket = tempTicket   
        print(userTicket)
        makeLotteryTicket()
        partialMatch(winningTicket, userTicket)
def partialMatch(a, b):
    print(f'winning:{a}')
    print(f'user: {b}')
    if a[0] == b[0]:
        print("you matched the first number")
        winnings.append(4)
    elif a[0:1] == b[0:1]:
        print("you matched the first two numbers")
        winnings.append(7)
    elif a[0:2] == b[0:2]:
        print("you matched the first three numbers")
        winnings.append(100)
    elif a[0:1] == b[0:3]:
        print("you matched the first four numbers")
        winnings.append(50000)
    elif a[0:4] == b[0:4]:
        print("you matched the first five numbers")
        winnings.append(1000000)
    elif a[0:5] == b[0:5]:
        print("You won the lotto!")
        winnings.append(25000000)
    elif a != b:
        print('Sorry no matches')
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

print(pick6())



#print(totalCost(cost))
#print(totalWinnings(winnings))