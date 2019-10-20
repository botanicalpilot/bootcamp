

listN = [1, 2, 3, 4, 5, 6]
tagertN = 7
def findingTarget(listN):
    for n in listN:
        deductedList = listN
        aN = n
        deductedList.remove(aN)
        for item in deductedList:
            if item + aN == tagertN:
                print(item, aN)
            else:
                break
       
print(findingTarget(listN))

'''
for each item in a list,
    add that item to another item in the list
    see if that item equals the target
        if yes, return both items in list
        if no, try again with 
    '''