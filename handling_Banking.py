class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance

    def getBalance(self):    
        return self.balance
    
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount    

class SavingAccount(Account):
    def __init__(self,title,balance,interestrate=0):
        super().__init__(title,balance)
        self.interestrate=interestrate

    def interestamount(self):    
        self.interest_amount=((self.interestrate * self.balance)/100)

a=Account("omk",500)
print(a.getBalance())
a.deposit(1000)
print(a.getBalance())
a.withdraw(400)
print(a.getBalance())

# output:
# 500
# 1500
# 1100

a=SavingAccount("omk",2000,5)
a.interestamount()
print(a.interest_amount)

# output:
# 100.0