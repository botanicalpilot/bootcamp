

'''
We need to look at each item in data and see if the items before and after it are lower/lower (peak) or high/high(valley). return the index number for all instances that occur. Then take the peaks and valleys function to return the index of all the peaks and valleys.
'''
import itertools

def enumData(data):
    #use enumerate to make a new list of tuples, index, with the items of (index,value) pairs
    indexData = list(enumerate(data, 1))
    return indexData

def displayData(indexData):
    for index, val in indexData:
        star = 'x' * val
        indexValue = index
        print(indexValue, star)
        #print(indexValue, val)

def peak(data):
    peaks = []
    for item in data:
        if data[x] > data[x+1] and data[x] > data[x-1]:
            peaks.append(item)
    return peaks
    

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8]
    indexData = enumerate(data)
    displayData(indexData)
    #print(valleys(data))
    print(peak(data))

main()


'how can I compare the items in a list or a truple to those in front and being them? and return the value of their index?'
