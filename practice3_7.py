def commoneElem(listA, listB):
    #using binary operator '&' to return results if excists in both oeprands
    #sets are themselves mutable, but their items are not. Therefore you cannot have a list inside a set. 
    #sets will not return multiples of the same item
    return set(listA) & set(listB)

listA = ['dog', 'cat', 'horse']
listB = ['moneky', 'dog', 'cat', 'snake']

print(commoneElem(listA, listB))