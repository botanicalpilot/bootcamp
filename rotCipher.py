'''
1. Need to convert user input string into list.
    words need to be split from eachother, and then split into individual letts
    make new list with only letters
2. match the list of letters to index number. index could be a key in the dictionary and the values could be the letter and the corrisponding letter. Does this dictionary need to be nested or should it have multiple values for each key?
3. Need some way to control offset for ciphered alphabet 
'''
import string

def cipher():
    letters = dict(string.ascii_lowercase)
    print(letters)
cipher()