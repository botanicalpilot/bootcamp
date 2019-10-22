fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

def combine(a,b):
    return dict(zip(a,b))

def averagePrice(combineResults):
    allValues = (sum(combineResults.values()) / len(combineResults))
    return allValues

    #return [(sum(value) / len(key)) for key, value in combineResults]
print(averagePrice(combine(fruits, prices)))

