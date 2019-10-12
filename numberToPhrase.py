def getNumber():
    numberToConvert = int(input("Enter a number between 1 and 999: "))
    return numberToConvert

def onesExtract(x):
    ones_digit = x%10
    return ones_digit

def onesConversion(x):
    oneMatch = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 0 : ''}
    if x in oneMatch:
        return oneMatch[x]

def tensExtract(x):
    tens_digit = x // 10
    removeHundred = tens_digit%10
    return removeHundred

def tensConversion(x):
    tenMatch = {1 : 'ONE', 2: 'twenty', 3 : 'thirty', 4: 'fourty', 5 : 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety', 0 : ''}
    if x in tenMatch:
        return tenMatch[x]

def teens(y):
    teensDic = {1 : 'eleven', 2 : 'twelve', 3 : 'thirteen', 4 : 'fourteen', 5 : 'fifteen', 6 : 'sixteen', 7 : 'seventeen', 8 : 'eighteen', 9 : 'nineteen'}
    if y in teensDic:
        return teensDic[y]

def hundreds(x):
    hundredPlace = x//100
    hundredMatch = {1 : 'one hundred', 2 : 'two hundred', 3 : 'three hundred', 4 : 'four hundred', 5 : 'five hundred', 6 : 'six hundred', 7 : 'seven hundred', 8 : 'eight hundred', 9 : 'ninehundred', 0 : ''}
    if hundredPlace in hundredMatch:
        return hundredMatch[hundredPlace]

    
def main():
    #get number from user wanting to convert
    userN = getNumber()

    #get digits in ones and tens place
    tenDigit = tensExtract(userN)
    oneDigit = onesExtract(userN)

    #convert number to digit
    tenWord = tensConversion(tenDigit)
    oneWord = onesConversion(oneDigit)
    
    #test if for teen N
    if tenWord == 'ONE':
        print(hundreds(userN))
        print(teens(oneDigit))
        
    else:
        print(hundreds(userN))
        print(tenWord)
        print(oneWord)
        
       
main()

