

toBeConverted = float(input("Welcome to the change conveter. Enter the dollar amount you want to convert (eg. 1.47) "))
total = toBeConverted*100

change = {
'quarters': 25,
'dimes': 10,
'nickels': 5,
'pennies': 1
}

for key, value in change.items():
    if total // value != 0:
        print(f'{total // value} {key}')
    else:
        continue
