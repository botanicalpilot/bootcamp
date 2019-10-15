'''

Convert the input string into a list of ints - done
Slice off the last digit. That is the check digit. - done
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid
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

def reverse(userCard):
    lastVal = userCard
    #del is a statement, like return. Using it anyother way will result in a 'not subscriptiable' TypeError
    del lastVal[-1]
    lastVal.reverse()
    return lastVal


#print(getUserCard())
#print(checkDigit(getUserCard()))
print(reverse(getUserCard()))