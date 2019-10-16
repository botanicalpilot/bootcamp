'''

Convert the input string into a list of ints - done
Slice off the last digit. That is the check digit. - done
Reverse the digits. - done
Double every other element in the reversed list. - done
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
minus last digit and reversed : 5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4
numbers to be doubled: 5, 9, 8, 8, 7, 7, 5, 4
doubled items :[10, 18, 16, 16, 14, 14, 10, 8]
remaining items:8, 9, 6, 5, 3, 6, 5
'''
#get card numbers
def getUserCard():
    inputUserCard = input('Enter each card number, followed by a space to validate: ')
    userCard = inputUserCard.split(' ')
    #convert list of string to int using map(callable, iter1, inter2...)
    userCard = list(map(int, userCard))
    return userCard

#get last digit
def checkDigit(userCard):
    userCheckDigit = userCard.pop(-1)
    return userCheckDigit

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



#print(getUserCard())
#print(checkDigit(getUserCard()))
#print()

def main():
    #lastVal equals the result of removing the last digit and reverse the resulting list. 
    lastVal = reverse(getUserCard())
    print(lastVal)

    #onlyDoubles takes lastVal and doubles every second item. It stores these values in new list. 
    onlyDoubles = doubleItems(lastVal)
    print(onlyDoubles)
    #remove doubled items from lastVal list
    lastValND = sum(removeDoubleItems(lastVal))
    subtracted = sum(subtractNine(onlyDoubles))
    print(lastValND + subtracted)
 
   
main()