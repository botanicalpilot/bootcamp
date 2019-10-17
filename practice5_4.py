import string
def asciiComprehension():
    return {char: ord(char) for char in string.ascii_lowercase }

print(asciiComprehension())