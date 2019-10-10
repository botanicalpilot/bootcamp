import string

def cipher():
    letters = string.ascii_lowercase
    userMessage = input("Enter your string you want deciphered: ")
    cipherLetters = letters[13:] + letters[:13]

    #print(cipherLetters)
    #cipherDic = dict(zip(letters, cipherLetters))
    #print(cipherDic)
    #def replace(userMessage,cipherDic):
    #userList = list(userMessage)
    table = str.maketrans(letters, cipherLetters)
    print(userMessage.translate(table))


   # replacedMessage = []
    #for l in userList:
        #replacedMessage.append(cipherDic.get(letters[cipherLetters]))
   # print(replacedMessage)


'''
I've tried two things without success and now i am at a loss. 
I first tried makeing a dictionary using zip with the offset in cipherLetters. That worked for making the dictionary, but then I couldn't replace the values from each letter into a new list that would display the ciphered text. 

I went back to making a table with maketrans and using that table to translate the userMessage into the ciphered text. I feel like I've read enough of this shit now that I understand how these are supposed to work, but I still can't get it to work with my code. 

I finally got it to work with the table. The problem was I was using 'return' rather than print. Return does just that, returns the value to the caller. Specifically it breaks out of the function you are in, and if you call that function elsewhere it will return the value. 

'''
cipher()
