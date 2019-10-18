def countKatzHund(katzenHundeString):
    cats = katzenHundeString.count('cat')
    dogs = katzenHundeString.count('dog')
    if dogs == cats:
        return True
    else:
        return False
print(countKatzHund('catdogcatdog'))