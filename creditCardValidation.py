
#get card numbers
def getUserCard():
    inputUserCard = input('Enter each card number, followed by a space to validate: ')
    userCard = inputUserCard.split(' ')
    #convert list of string to int using map(callable, iter1, inter2...)
    userCard = list(map(int, userCard))
    return userCard

#remove last digit
def checkDigit(userCard):
    userCheckDigit = userCard.pop(-1)
    return userCheckDigit

def getLastDig(userCard):
    lastDig = userCard[-1]
    return lastDig

#remove the last item in the list and return the list reversed
def reverse(userCard):
    lastVal = userCard
    #del is a statement, like return. Using it anyother way will result in a 'not subscriptiable' TypeError
    del lastVal[-1]
    lastVal.reverse()
    return lastVal

#double every second item in list from def reverse(userCard). 
def doubleItems(lastVal):
    doubled = list(map((lambda x: x * 2), lastVal[::2]))
    return doubled

#remove items that were doubled from lastVal
def removeDoubleItems(lastVal):
    del lastVal[::2]
    return lastVal

#take return value from doubleItems(lastVal). Error with this function, it is not adding in the items that are less that 10
def subtractNine(doubled):
    minusNine = [ x - 9 if x >= 10 else x for x in doubled]
    return minusNine
#take the last digit of total and compare it to the last number from user input
def secondOfSum(total, lastVal):
    if total % 10 == getLastDig(lastVal):
        return True
    else: 
        return False
    

def main():
    lastVal = reverse(getUserCard())
    onlyDoubles = doubleItems(lastVal)
    lastValND = sum(removeDoubleItems(lastVal))
    subtracted = sum(subtractNine(onlyDoubles))
    total = lastValND + subtracted
    lastValue = getLastDig(lastVal)
    print(secondOfSum(total, lastVal))
 
   
main()