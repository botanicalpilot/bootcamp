def sum_pairs(ints, s):
    for item in ints:
        ints[item] + item for item if 
	pass
print(sum_pairs([1, 4, 8, 7, 3, 15], 8))












'''
////Sum of digits\\\\
maybe try using recursion in this!

def digital_root(n):
    stringN = str(n)
    tmp = ''
    
    def findingSum(stringN):
        strDigN = [int(i) for i in stringN]
        sumStrDig = sum(strDigN)
        if sumStrDig < 10:
            return sumStrDig
        else: 
            tmp = str(sumStrDig)
    findingSum(stringN)
    print(tmp)


    
    function idea for sum of digits
        takes strDigits, replaces them with ints
        sum ints
            if sum of digiits is less than ten
            return sum
            else
            return  strdigits
        
print(digital_root(67))
'''

'''
def findLargest(N):
    mylist = [0] * 3
    print(mylist)
    for i in mylist:
        if 3 ** i < N:
            return i



print(findLargest(4))

'''



 









'''
mexican wave
def wave(strng):
    strng.lower()
    waveStr = []
    for item in strng:
        if item != ' ':
            waveStr.append(strng.replace(item, item.capitalize(), 1))
    return waveStr
'''

            

            
    