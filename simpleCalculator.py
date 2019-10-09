
def main():
    userOperator = input('What operation would you like to perform? ')
    firstN = float(input('What is your first number? '))
    secondN = float(input('What is your second number? '))

    def plus(x, y):
        result = firstN + secondN
        if userOperator == '+':
            print(result)
    def minus(x, y):
        result = firstN - secondN
        if userOperator == '-':
            print(result)
    def multiply(x, y):
        result = firstN * secondN
        if userOperator == '*':
            print(result)
    def divide(x, y):
        result = firstN / secondN
        if userOperator == '/':
            print(result)

    simpleCalc = {
        '+' : plus(firstN, secondN),
        '-' : minus(firstN, secondN),
        '*' : multiply(firstN, secondN),
        '/' : divide(firstN, secondN),
    }
'''
    def calculate(userOperator):
        if userOperator == '+':
            print(simpleCalc['+']())

        elif userOperator == '-':
            print(simpleCalc['-']())

        elif userOperator == '*':
            print(simpleCalc['*']())

        elif userOperator == '/':
            print(simpleCalc['/']())
'''
main()