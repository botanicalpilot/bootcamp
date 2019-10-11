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
    winningTicket = []
    for n in range(6):
        winningTicket.append(random.choice(range(1,99)))
    return winningTicket

def makeLotteryTicket():
    userTicket = []
    for n in range(6):
        userTicket.append(random.choice(range(1,99))) 
    return userTicket 
        
def partialMatch(lista, listb):
    totalWinnings = []
    if lista[0:5] == listb[0:5]:
        #print(f"You won the lotto!")
        totalWinnings.append(25000000)
    if lista[0:4] == listb[0:4]:
        #print(f"you matched the first five numbers{listb}")
        totalWinnings.append(1000000)
    if lista[0:3] == listb[0:3]:
        #print(f"you matched the first four numbers {listb}")
        totalWinnings.append(50000)
    if lista[0:2] == listb[0:2]:
        #print(f"you matched the first three numbers {listb}")
        totalWinnings.append(100)
    if lista[0:1] == listb[0:1]:
        #print(f"you matched the first two numbers {listb}")
        totalWinnings.append(7)
    if lista[0] == listb[0]:
        #print(f"you matched the first number {listb}")
        totalWinnings.append(4)
    return totalWinnings
    
def totalCost(a):
    total = 0
    for n in a:
        total += n
    return total

def allWins(a):
    winningsEarned = 0
    for n in a:
        winningsEarned += n
    return winningsEarned

def main():
    winningTicket = pick6()
    cost = []
    for n in range(100000):
        cost.append(2)
        userTicket = makeLotteryTicket()
        totalWinnings = partialMatch(winningTicket, userTicket)
        print(totalWinnings)

    print(winningTicket)
    print(f'Total earnings: {allWins(totalWinnings)}')
    print(f'Total cost: {totalCost(cost)}')
    
main()
