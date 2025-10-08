class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

acc = BankAccount("Disha", 1000)
print(f"Owner: {acc.owner}, Opening Balance: {acc.balance}")
acc.deposit(500)
print("Amount after deposit")
print(f"Owner: {acc.owner}, Balance: {acc.balance}")
acc.withdraw(300)
print("Amount after withdraw")
print(f"Owner: {acc.owner}, Balance: {acc.balance}")
