def evenNumbers():
    numbers = list(range(21))
    print(numbers)
    return [x for x in numbers if x % 2 == 0]

print(evenNumbers())