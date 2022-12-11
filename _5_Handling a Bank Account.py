class Account:
    def __init__(self,title,balance=0):
        self.title=title
        self.balance=balance
    def withdrawal(self, amount):
        self.balance=self.balance-amount
    def deposit(self,amount):
        self.balance=self.balance+amount
    def getBalance(self):
        return self.balance
class SavingAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def interestAmount(self):
        interest_amount=((self.interestRate*self.balance)/100)
        return interest_amount

demo1=SavingAccount("Ashish",2000,5)
demo1.deposit(500)
print(f"After deposite total balance :{demo1.getBalance()}")

demo1.withdrawal(500)
print(f"After withdrawal balance:{demo1.getBalance()}")

print(f"Interest on the current balance:{demo1.interestAmount()}")





