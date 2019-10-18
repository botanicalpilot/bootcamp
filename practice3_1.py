import random

def randomElement(a):
    n = random.randint(0, (len(a) -1 ))
    return a[n]

aList = ['lions', 'tigers', 'bears', 'jesus']
print(randomElement(aList))