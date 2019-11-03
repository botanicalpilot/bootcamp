def valid_parentheses(string):
    if string == "":
        return True
    listPar = [item for item in string if item == ')' or item == '(']
    #print(f'Listpar: {listPar}')
    if listPar.count('(') != listPar.count(')'):
        return False
    else:
        stringPar = ''.join(listPar)
        #print(f'stringPar: {stringPar}')
        removeMatch = stringPar.replace('()', '')
        #print(f'removeMatch: {removeMatch}')
        if removeMatch == '':
            return True
        else:
            return False
        


print(valid_parentheses("(c(b(a)))(d)"))













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

            

            
    