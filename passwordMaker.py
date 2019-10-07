import random
import string

def makePassword():
    "Welcome to the password generator! Answer the following promts to make your password!"
    upper = int(input("Of those characters, how many do you want to be uppercase? "))
    lower = int(input("Of those characters, how many do you want to be lowercase? "))
    numbers = int(input("Of those characters, how many do you want to be numbers? "))
    special = int(input("Of those characters, how many do you want to be special characters? "))

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    usernumbers = string.digits
    userspecial = ['!', '@', '#', '$', '%', '^', '&', '*']

#Create a empty password list, append list in each for loop.
    password = []
    for i in range(upper):
        password.append(random.choice(uppercase))
    for i in range(lower):
        password.append(random.choice(lowercase))
    for i in range(numbers):
        password.append(random.choice(usernumbers))
    for i in range(special):
        password.append(random.choice(userspecial))

#shuffle password list, join and then print.
    random.shuffle(password)
    print(''.join(password))


makePassword()
