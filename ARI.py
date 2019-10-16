'''
first get number of sentences, assign to variable
get numer of words, assign to variable
    will need to remove punctuation
get number of characters, assign to variable
'''
import string



#split up book into list by period. This doesn't do a perfect job so this function could be improved with conditional statements
#May checking if there is a period followed by a capitalized letter?
def sentences(contents):
    sentencesInBook = str(contents.split('.'))
    return len(sentencesInBook)

#removes punctuation like I did in countWords.py. Returns a string. 
def removePunct(contents):
    lower = contents.lower()
    table = str.maketrans('', '', string.punctuation)
    return lower.translate(table)

#use removePunct as parameter. Counts number of words. Could be improved by removing the '/n' from book. 
def wordCount(removePunct):
    words = str(removePunct.split(' '))
    #print(words)
    return len(words)

def characterCount(removePunct):
    characters = removePunct
    #totalCharacters = list(characters)
    #print(totalCharacters)
    #print(characters)
    return len(characters)
    
def ARI_calc(characters, words, sentences):
    return 4.71 * (characters / words) + 0.5 *(words / sentences) - 21.43
    
# for some reason word count is returning with a higher value that character count. No idea why. 
#print(f'wordcount: {wordCount(removePunct(contents))}')
#print(f'character count: {characterCount(removePunct(contents))}')

def main():
    botanyBook = open('botanyBookSample.txt')
    contents = botanyBook.read()
    characters = characterCount(removePunct(contents))
    words = wordCount(removePunct(contents))
    sentencesInBook = sentences(contents)
    print(ARI_calc(characters, words, sentencesInBook))
main()