def listN():
    numbers = []
    while True:
        userNums = input("Type and enter numbers. When finished enter 'done': ")
        if userNums != 'done':
            numbers.append(int(userNums))
        else:
            break
    return numbers

print(listN())
