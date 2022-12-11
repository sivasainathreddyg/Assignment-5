class Account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
class SavingAccount(Account):
    def __init__(self,interesrRate):
        self.intrestRate=interesrRate

account=Account("Ashish",5000)
savingaccount=SavingAccount(5)

