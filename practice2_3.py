def lastLetter(uString):
    sortedString = list(uString)
    sortedString.sort()
    return sortedString[-1]

print(lastLetter('buttcrack'))
