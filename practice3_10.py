def mergeListsZip(listA, listB):
    return [list(s) for s in zip(listA, listB)]
listA = [1, 2, 3]
listB = ['a', 'b', 'c']
print(mergeListsZip(listA, listB))
