class ATM:
    def __init__(self, amount = 0, balance = [], transactionHistory = []):
        self.balance = balance
        self.amount = amount
        self.tranasctionHistory = transactionHistory
    def __repl__(self):
        return self.deposit 
        return self.withdraw 
        return self.checkBalance 
        return self.tranasctionHistory

    def checkBalance(self):
        return self.balance

    def deposit(self, amount):
        self.tranasctionHistory.append(f'deposited: {amount}')
        return amount + self.balance
        

    def checkWithdrawal(self):
        if self.balance >= self.amount:
            return True
        else:
            return False

    def withdraw(self, amount):
            self.tranasctionHistory.append(f'withdrew: {amount}')
            #self.balance. append(- self.amount)
            return self.balance - amount

    def transactions(self):
        return self.tranasctionHistory


def main():
    p1 = ATM(0, 0, [])
    startingBalance = int(input("What is the starting balance for the account? "))
    p1.balance = startingBalance
    while True:
        toDo = input("Enter would you like to do. 'Check balance', 'deposit', 'withdraw', or see your history with 'transactions': ").lower()
        if toDo =='deposit':
            deposit = int(input('How much would you like to deposit? '))
            # action = ATM(deposit, startingBalance).deposit()
            p1.balance = p1.deposit(deposit)
            print(p1.balance)
        elif toDo == 'withdraw':
            withdraw = int(input('How much would you like to withdraw? '))
            if p1.checkWithdrawal == True:
                p1.balance = p1.withdraw(withdraw)
                #action = ATM(withdraw, startingBalance).withdraw()
                print(p1.balance)
            else:
                print('insufficient funds')
        elif toDo == 'check balance':
            #action = ATM(0, startingBalance).checkBalance()
            print(p1.balance)
        elif toDo == 'transactions':
            action = p1.transactions()
            print(action)
        else:
            break

main()
        
'''
one isse I am having is with balance. I may need to ask the user for their  starting balance, but that seems like it is breaking the instructions for the lab. 

'''