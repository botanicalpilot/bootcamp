class ATM:
    def __init__(self, amount, balance = 0, transactionHistory = []):
        self.balance = balance
        self.amount = amount
        self.tranasctionHistory = transactionHistory

    def checkBalance(self):
        return self.balance

    def deposit(self):
        self.tranasctionHistory.append(f'deposited: {self.amount}')
        return self.balance + self.amount

    def checkWithdrawal(self):
        if self.balance >= self.amount:
            return True
        else:
            return False

    def withdraw(self):
            self.tranasctionHistory.append(f'withdrew: {self.amount}')
            return self.balance - self.amount

    def transactions(self):
        return self.tranasctionHistory

        

test = ATM(20, 35)
print(test.withdraw(), test.deposit(), test.transactions())