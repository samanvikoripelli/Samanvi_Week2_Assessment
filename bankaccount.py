class BankAccount:
    def __init__(self,balance = 0):
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"deposit {amount}")
        else:
            print("invalid deposit amount")
    def withdraw(self,amount):
        if  amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"withdraw {amount}")
            else:
                print("insufficient balance withdraw denied")
        else:
            print("invalid withdrawal amount")
    def get_balance(self):
        return self.balance
account = BankAccount(200)
account.deposit(100)
account.withdraw(300)
account.withdraw(50)
print(f"final balance:{account.get_balance()}")