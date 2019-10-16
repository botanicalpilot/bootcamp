'''
Open the file.done
Make everything lowercase, strip punctuation, split into a list of words.done
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count. done
Print the most frequent top 10 out with their counts. You can do that with the code below.
'''
import string


def getEditBook():
    #F/I book
    botanyBook = open('botanyBook.txt')

    #read book, lower contents
    contents = botanyBook.read()
    contentsLower = contents.lower()

    #remove punctuation
    #create a three argument translation table (x, y, and z). x and y must be equal length strings/characters. 
    #Characters/strings in x are replaced by characters in y. string.punction is therefore mapped to None. 
    punctuationTable = str.maketrans('','', string.punctuation)
    noPunct = contentsLower.translate(punctuationTable)

    #seperate all words into list
    words = noPunct.split(" ")
    return words
'''
#remove the spaces from the getEditBook() function   
def removeSpaces(words):
    for item in words:
        if item == '':
            words.remove(item)
    return words
'''

def wordCount(words):
    totalCount = dict()
    for item in words:
        #get item from words, default value is 0. Add one if present. 
        totalCount[item] = totalCount.get(item, 0) +1
    return totalCount


    
def main():
    totals = wordCount(getEditBook())
    words = list(totals.items())
    words.sort(key=lambda tup: tup[1], reverse=True)  
    for i in range(min(10, len(words))):  
        print(words[i])

main()




