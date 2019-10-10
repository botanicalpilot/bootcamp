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
    print(winningTicket)
    for n in range(100000):
        userTicket = random.choice(range(1,99))
        cost = 0
        
        

pick6()