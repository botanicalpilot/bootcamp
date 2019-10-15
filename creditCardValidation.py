'''

Convert the input string into a list of ints - done
Slice off the last digit. That is the check digit. - done
Reverse the digits. - done
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
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

#double every second item in list from def reverse(userCard). Do I need to even make a function here?
def doubleItems(lastVal):
    return list(map((lambda x: x * 2), lastVal[::2]))



#print(getUserCard())
#print(checkDigit(getUserCard()))
#print()

lastVal = reverse(getUserCard())
print(doubleItems(lastVal))