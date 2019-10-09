'''
make a list of numbers from user input
make a running sum of that list of numbers
divide final sum by the number of elements in the list

maybe use the * discussed yesterday in class
'''
import string

def getNumbers():
    finalN = []
    while True:
        userN = input("Enter numbers you want to averge. When finished, type 'done': ")
        if userN.isdigit():
            finalN.append(userN)
            print(finalN)
        else:
            break
