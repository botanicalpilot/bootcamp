import random
import string

def makePassword():
    length = int(input("How many characters long do you want your password to be? "))
    letters = string.ascii_letters
    password = []
    for i in range(length):
        password.append(random.choice(letters))
    print(''.join(password))
    
makePassword()
