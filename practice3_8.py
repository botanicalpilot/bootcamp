def combine(listA, listB):
    #create a list with nothing in it. Multiply it by the total len of the lists taken by the function
    combined = [None]*(len(listA) + len(listB))
    #assign every other item in combined list to listA items starting at 0
    combined[::2] = listA
    #assign every other item in combined list to listB items starting at 1
    combined[1::2] = listB
    return combined
      
print(combine([1, 2, 3], ['a', 'b', 'c']))
    