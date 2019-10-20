nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def mergeAll(nums):
    #emptyNums = []
    #for x in nums:
        #for y in x:
            #emptyNums.append(y)
    #return emptyNums
    
    #same as above, but in nested list comprehension
    return [y for x in nums for y in x]
print(mergeAll(nums))

