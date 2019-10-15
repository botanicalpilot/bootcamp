
import random

def hitBustedBlackjack(total):
    if total == 21:
        print('Blackjack!')
    elif total < 17:
        print('hit')
    elif 17 <= total < 21:
        print('stay')
    else:
        print('busted')


def getValues(list, cardDict):
    total = []
    for x in list:
        if x in cardDict:
            total.append(cardDict[x])
    return sum(total)

def randomCards(cards):
    choosesCards = []
    for i in range(3):
        choosesCards.append(random.choice(cards))
    return choosesCards
        

def main():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cardValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    cardDict = dict(zip(cards, cardValue))
    userCards = randomCards(cards)
    print(f'Your cards are {userCards}')
    total = getValues(userCards, cardDict)
    hitBustedBlackjack(total)

main()