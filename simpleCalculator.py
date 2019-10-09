


def plus(firstN, secondN):
    firstN + secondN
def minus(firstN, secondN):
    firstN - secondN
def multiply(firstN, secondN):
    firstN * secondN
def divide(firstN, secondN):
    firstN / secondN

simpleCalc = {
    '+':plus()
    '-':minus()
    '*':multiply()
    '/':divide()
}
def getUserInput():
    userOperator = input('What operation would you like to perform? ')
    firstN = float(input('What is your first number?'))
    secondN = float(input('What is your second number?')
