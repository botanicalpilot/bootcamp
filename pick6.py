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
winningTicket = []
winnings = []


def pick6():
    for n in range(6):
        winningTicket.append(random.choice(range(1,99)))
    #print(winningTicket)

def testingLotteryTicket():
    print(f'winning ticket:{winningTicket}')
    for n in range(100):
        userTicket = []
        def makeLotteryTicket(userTicket):
            tempTicket = []
            for n in range(6):
                tempTicket.append(random.choice(range(1,99)))  
            userTicket = tempTicket   
            print(userTicket)
        makeLotteryTicket(userTicket)
        partialMatch(winningTicket, userTicket)
        ''' 
        if any(elem in winningTicket for elem in userTicket):
            print("you got a match!")
            partialMatch(winningTicket, userTicket)
            cost.append(2)
            makeLotteryTicket(userTicket)
        elif userTicket != winningTicket:
            cost.append(2)
            makeLotteryTicket(userTicket)
            #print("sorry no matches")
        else:
            print('error')
'''
def partialMatch(winningTicket, userTicket):
    if winningTicket[0] == userTicket[0]:
        print("you matched the first number")
        winnings.append(4)
    elif winningTicket[0:1] == userTicket[0:1]:
        print("you matched the first two numbers")
        winnings.append(7)
    elif winningTicket[0:2] == userTicket[0:2]:
        print("you matched the first three numbers")
        winnings.append(100)
    elif winningTicket[0:1] == userTicket[0:3]:
        print("you matched the first four numbers")
        winnings.append(50000)
    elif winningTicket[0:4] == userTicket[0:4]:
        print("you matched the first five numbers")
        winnings.append(1000000)
    elif winningTicket[0:5] == userTicket[0:5]:
        print("You won the lotto!")
        winnings.append(25000000)
    elif winningTicket != userTicket:
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

pick6()
testingLotteryTicket()


print(totalCost(cost))
print(totalWinnings(winnings))