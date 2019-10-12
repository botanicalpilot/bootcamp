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

main()