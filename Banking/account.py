class Account(object):
    def __init__(self,balance):
        self.balance = float(balance)

    def getBalance(self):
        return self.balance
    def deposit(self,amt):
        if float(amt) > 0:
            self.balance+=float(amt)
    def withdraw(self,amt):
        if float(amt) < 0:
            self.balance-=float(amt)