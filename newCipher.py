import string

def cipher():
    letters = string.ascii_lowercase
    userMessage = input("Enter your string you want deciphered: ").lower()
    #make the shifted letter list for the table below. start at position 13 in letters and go to end of list. Add the begining of the list up to the 13th item. 
    cipherLetters = letters[13:] + letters[:13]
    #make a table with maketrans(charcter, mappedCharacter)
    table = str.maketrans(letters, cipherLetters)
    #translate the message using the table. 
    print(userMessage.translate(table))

cipher()


'''
Things I tried:
I first tried makeing a dictionary using zip with the offset in cipherLetters. That worked for making the dictionary, but then I couldn't replace the values from each letter into a new list that would display the ciphered text. 

I went back to making a table with maketrans and using that table to translate the userMessage into the ciphered text. I feel like I've read enough of this shit now that I understand how these work. 

I finally got it to work with the table. One problem I was having was because I was using 'return' rather than print. Return does just that, returns the value to the caller. Specifically it breaks out of the function you are in, and if you call that function elsewhere it will return the value. 

'''

