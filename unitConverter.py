
ft = float(0.3048)
mi = float(1609.34)
m = 1
km = m * 1000
yd = float(0.9144)
inches = float(0.0254)
converted = dict()

#convert the og value (userValue) to meters. Use the unit given to reference global variables.
def conversionToMeters(userUnit, userValue):
    if userUnit == 'ft':
        toMeters = ft * userValue
        converted['firstConverion'] = toMeters
        print(converted)
    elif userUnit == 'km':
        toMeters = km * userValue
        converted['firstConverion'] = toMeters
        print(converted)
    elif userUnit == 'mi':
        toMeters = mi * userValue
        converted['firstConverion'] = toMeters
        print(converted)
    elif userUnit == 'yd':
        toMeters = yd * userValue
        converted['firstConverion'] = toMeters
        print(converted)
    elif userUnit == 'in':
        toMeters = inches * userValue
        converted['firstConverion'] = toMeters
        print(converted)
    elif userUnit == 'm':
        toMeters == UserValue
        converted['firstConverion'] = toMeters
        print(converted)
    else:
        print('invalid user input')
        return

#convert from meters to whatever value indicated by user in userConvertedUnit
def conversiontoUnits():
    if 'ft' in converted:
        result = ft * converted['firstConverion']
        converted['finalconversion'] = result
        print(converted)
    if 'km' in converted:
        result = km * converted['firstConverion']
        converted['finalconversion'] = result
        print(converted)
    if 'mi' in converted:
        result = mi * converted['firstConverion']
        converted['finalconversion'] = result
        print(converted)
    if 'yd' in converted:
        result = yd * converted['firstConverion']
        converted['finalconversion'] = result
        print(converted)
    if 'in' in converted:
        result = inches * converted['firstConverion']
        converted['finalconversion'] = result
        print(converted)
    if 'm' in converted:
        result = converted['firstConverion']
        converted['finalconversion'] = result
        print(converted)

def main():
    userDistance = input("What distance do you want to convert? Enter your number followed by unit abberviation - 'km', 'm' 'mi', 'ft', 'yd', 'in' (eg. '145 ft'): ").split(" ")
    userValue = int(userDistance[0])
    userUnit = userDistance[1]
    userConvertedUnit = input("What unit do you want to convert to? ")

    converted[userConvertedUnit] = None
    conversionToMeters(userUnit, userValue)
    conversiontoUnits()
    print(f"{userValue} {userUnit} is {converted['finalconversion']} {userConvertedUnit}")

main()
