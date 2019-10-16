'''
first get number of sentences, assign to variable
get numer of words, assign to variable
    will need to remove punctuation
get number of characters, assign to variable
'''
import string
import math

ariScale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


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
    
def ariCalc(characters, words, sentences):
    #using ceiling from math to return the rounded up value from the function below. 
    #because my character count is not working, I have to take the absolute value (abs)
    score = math.ceil(abs( 4.71 * (characters / words) + 0.5 *(words / sentences) - 21.43))
    if score > 14:
        return 14
    else:
        return score

'''
issues:
for some reason word count is returning with a higher value that character count. No idea why. 
#print(f'wordcount: {wordCount(removePunct(contents))}')
#print(f'character count: {characterCount(removePunct(contents))}')
'''

def main():
    botanyBook = open('botanyBookSample.txt')
    contents = botanyBook.read()
    characters = characterCount(removePunct(contents))
    words = wordCount(removePunct(contents))
    sentencesInBook = sentences(contents)
    ariScore = ariCalc(characters, words, sentencesInBook)
    #print(ariScore)
    print(ariScale[ariScore])


#Run the program    
main()