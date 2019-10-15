
import random

#evaluate for Aces in userCards, and total
def aceEval(userCards, total):
    aCount = userCards.count('A')
    aValue = []
    if aCount == 1:
        if total <= 10:
            aValue.append(11)
            aValue.append(total)
        else:
            aValue.append(1)
            aValue.append(total)
    else:
        aValue.append(2)
    return sum(aValue)

#
def hitBustedBlackjack(total):
    if total == 21:
        print('Blackjack!')
    elif total < 17:
        print('hit')
    elif 17 <= total < 21:
        print('stay')
    else:
        print('busted')

#get values from list (userCards)
def getValues(list, cardDict):
    total = []
    for x in list:
        if x in cardDict:
            total.append(cardDict[x])
    return sum(total)

#randomly choose three cards for our players. Take the input cards from the main functions. 
def randomCards(cards):
    choosesCards = []
    for i in range(3):
        choosesCards.append(random.choice(cards))
    return choosesCards
        

def main():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cardValue = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    cardDict = dict(zip(cards, cardValue))
    print(cardDict)
    userCards = randomCards(cards)
    print(f'Your cards are {userCards}')
    if 'A' in userCards:
        totalNoA = getValues(userCards, cardDict)
        totalWA = aceEval(userCards, totalNoA)
        print(totalWA)
        hitBustedBlackjack(totalWA)

    else:    
        total = getValues(userCards, cardDict)
        print(f'Your total is {total}')
        hitBustedBlackjack(total)

main()
