
def userString():
    uString = input("enter a string: ")
    return''.join([letter * 2 for letter in uString])
print(userString())

