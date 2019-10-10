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
   letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   userInput = unicode(input("Enter your string you want deciphered: "), "UTF-8")
   userRot = int(input("Enter the offset you want for your cipher: "))
   cipheredInput = letters[userRot:] + letters[:userRot]
    #make translation table from letters to cipheredInput
   cipherTable = str.maketrans(letters, cipheredInput)
   #translate with the cipherTable using the int form the user. 
   userRot.translate(cipherTable)
 
cipher()