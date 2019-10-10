'''
1. Need to convert user input string into list.
    words need to be split from eachother, and then split into individual letts
    make new list with only letters
2. match the list of letters to index number. index could be a key in the dictionary and the values could be the letter and the corrisponding letter. Does this dictionary need to be nested or should it have multiple values for each key?
3. Need some way to control offset for ciphered alphabet 
'''
import os
import string


def cipher():
    #list is lowercase,uppercase,digits(0-9)
    letters = (string.ascii_letters + string.digits)
    userMessage = input("Enter your string you want deciphered: ")
    userShift = int(input("Enter the offset you want for your cipher: "))
    def shift(userShift):
        #make a new variable. Use return to call value to caller
        return letters[userShift:] + letters[:userShift]

#cipher()
letters = (string.ascii_letters + string.digits)
print(letters)


'''
I feel like at this point I am researching and working on things above my level. I will finish this code, but first complete the code that I believe I should be doing in another program called 'newCipher.py
'''