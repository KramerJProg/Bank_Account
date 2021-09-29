class BankAccount:
    def __init__(self, int_rate = .1, balance = 40):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        penalty = 5
        if self.balance > amount:
            self.balance -= amount
        else:
            self.balance -= penalty
            print("Insufficient funds: Charging a $5 fee.")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            addedInt = self.balance * self.int_rate
            self.balance += addedInt
        return self


account1 = BankAccount()
account2 = BankAccount()

account1.deposit(10).deposit(20).deposit(30).withdraw(50).yield_interest().display_account_info()

account2.deposit(20).deposit(40).withdraw(5).withdraw(7).withdraw(3).withdraw(13).yield_interest().display_account_info()
