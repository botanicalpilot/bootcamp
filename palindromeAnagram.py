def getLists():
    userWord = input("Enter a word to test for palindrome: ")
    letters = list(userWord)
    return letters

def check_palidrome(wordList):
    palidrome = wordList[::-1]
    if palidrome == wordList:
        return True

def main():
    wordList = getLists()
    print(check_palidrome(wordList))

#uncomment main, and comment out the print on line 32, to run palidrome version
#main()

def getAnagramOne():
    anagramPhraseOne = input("Enter a phrase to test for anagram: ").lower().replace(' ', '', -1)
    return anagramPhraseOne
    
def getAnagramTwo():
    anagramPhraseTwo = input("Enter a second phrase to test for anagram: ").lower().replace(' ', '', -1)
    return anagramPhraseTwo

def getAnagramList(AnagramOne, AnagramTwo):
    anagramLettersOne = list(AnagramOne)
    anagramLettersTwo = list(AnagramTwo)
    if sorted(anagramLettersOne) == sorted(anagramLettersTwo):
        return True

print(getAnagramList(getAnagramOne(), getAnagramTwo()))