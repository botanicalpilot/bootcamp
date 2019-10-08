
ft = float(0.3048)
mi = float(1609.34)
m = 1
km = m * 1000
yd = float(0.9144)
inches = float(0.0254)

def userToMeters():
    userDistance = input("What distance do you want to convert to meters? Enter your number followed by unit abberviation - 'km', 'mi', 'ft', 'yd', 'in' (eg. '145 ft'): ").split(" ")
    userValue = int(userDistance[0])
    userUnit = userDistance[1]

def userToUnits():
    userDistance = input("What distance do you want to convert? Enter your number followed by unit abberviation - 'km', 'mi', 'ft', 'yd', 'in' (eg. '145 ft'): ").split(" ")
    userValue = int(userDistance[0])
    userUnit = userDistance[1]
    userConvertedUnit = input("What unit do you want to convert to? ")

def converstionToMeters():
    userToMeters()
    if userUnit == 'ft':
        toMeters = ft * userValue
        #print(f'{userValue} {userUnit} is {ft * userValue} meters')

    elif userUnit == 'km':
        toMeters = km * userValue
        #print(f'{userValue} {userUnit} is {km * userValue} meters')

    elif userUnit == 'mi':
        toMeters = mi * userValue
        #print(f'{userValue} {userUnit} is {mi * userValue} meters')

    elif userUnit == 'yd':
        toMeters = yd * userValue
        #print(f'{userValue} {userUnit} is {yd * userValue} meters')
    elif userUnit == 'in':
        toMeters = inches * userValue
        #print(f'{userValue} {userUnit} is {inches * userValue} meters')

def conversionToUnits():
    userToUnits()
    converstionToMeters()
    if userConvertedUnit == 'ft':
        result = ft * toMeters
        print(result)
    elif userConvertedUnit == 'km':
        result = km * toMeters
        print(result)
    elif userConvertedUnit == 'mi':
        result = mi * toMeters
        print(result)
    elif userConvertedUnit == 'yd':
        result = yd * toMeters
        print(result)
    elif userConvertedUnit == 'in':
        result = inches * toMeters
        print(result)

conversionToUnits()
