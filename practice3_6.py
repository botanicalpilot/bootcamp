def extractLessThanTen(aList):
    lessTen = []
    for item in aList:
        if item < 10:
            lessTen.append(item)
    return lessTen
print(extractLessThanTen([1, 3, 11, 23, 5]))