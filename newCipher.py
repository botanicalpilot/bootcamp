import string

def cipher():
    letters = [string.ascii_letters]
    userMessage = input("Enter your string you want deciphered: ")
    cipherLetters = [letters[13:] + letters[:13]]
    print(cipherLetters)
    cipherDic = dict(zip(letters, cipherLetters))
    print(cipherDic)


cipher()