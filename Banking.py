class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance

class SavingAccount(Account):
    def __init__(self,title,balance,interestrate=0):
        super().__init__(title,balance)
        self.interestrate=interestrate

a=SavingAccount("omkar",5000,5)  
print(a.title)
print(a.balance)
print(a.interestrate)

# output:
# omkar
# 5000
# 5