
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8]
'''
We need to look at each item in data and see if the items before and after it are lower/lower (peak) or high/high(valley). return the index number for all instances that occur. Then take the peaks and valleys function to return the index of all the peaks and valleys.
'''
def display(data):
    #use enumerate to make a new list of tuples, index, with the items of (index,value) pairs
    indexData = list(enumerate(data, 1))
    print(indexData)
    for index, val in indexData:
        star = 'x' * val
        indexValue = index
        print(indexValue, star)
    
#def valleys():


#def peaksAndValleys():

print(display(data))