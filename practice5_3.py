aDict = {'a' : 1, 'b' : 2}

def swapKeyValue(aDict):
    return {key: value for value, key in aDict.items()}
print(swapKeyValue(aDict))
