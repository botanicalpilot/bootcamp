'''
make a list of numbers from user input
make a running sum of that list of numbers
divide final sum by the number of elements in the list

maybe use the * discussed yesterday in class
'''
import string
finalN = []
def getNumbers():
    while True:
        userN = input("Enter numbers you want to averge. When finished, type 'done': ")
        if userN.isdigit():
            finalN.append(userN)
            print(finalN)
        else:
            break
def averageNumbers():
    #make each item, in finalN, a float if that item is a number.
    conversionToFloat = [float(n) for n in finalN if n]
    print(conversionToFloat)
    #ternery operator approach: a if condition else b.
    #condition is evaluated to be True of False(booleant). If True, only a is evaluated; if False, only b is evaluated. Assign condition to averagedNumbers.
    #conditional expressions are very useful when in a 'one value or another' situation.
    averagedNumber = sum(conversionToFloat)/len(conversionToFloat) if conversionToFloat else '-'
    print(averagedNumber)

getNumbers()
averageNumbers()
