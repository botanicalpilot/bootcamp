print((2 ** 9))

def powersTwo(x):
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return[x ** y for y in range(10)]
print(powersTwo(2))