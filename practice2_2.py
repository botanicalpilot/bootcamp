def missingChar(someString):
    return [someString.replace(letter, '') for letter in someString]

   
print(missingChar('cardinal'))