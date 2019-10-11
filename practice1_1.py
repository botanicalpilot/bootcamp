def isEven(a):
    if a % 2 == 0:
        print(f'{a} is even')
    else:
        return
def isOdd(a):
    if a % 2 != 0:
        print(f'{a} is odd')
    else:
        return
def mainEvenOdd(a):
    isEven(a)
    isOdd(a)
mainEvenOdd(3)