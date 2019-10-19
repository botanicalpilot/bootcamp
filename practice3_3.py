def evenNN(numberList):
    evenList = []
    for number in numberList:
        if number % 2 == 0:
            evenList.append(numberList)
    if len(evenList) % 2 == 0:
        return True
    else:
        return False
print(evenNN([2,3,4, 5, 7, 6]))


 