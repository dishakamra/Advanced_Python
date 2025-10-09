"""
Create a BankAccount class that supports:
Printing the account balance --> __str__
Adding two accounts together --> __add__
Comparing accounts by balance --> __lt__, __eq__
Getting account lenth (number of transactions) --> __len__
Accessing transactions by index --> __getitem__
""" 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []  # Track deposits and withdrawals

    # Print representation
    def __str__(self):
        return f"Account({self.owner}) - Balance: ${self.balance}"

    # Add two accounts together
    def __add__(self, other):
        new_owner = f"{self.owner} & {other.owner}"
        new_balance = self.balance + other.balance
        return BankAccount(new_owner, new_balance)

    # Compare by balance
    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    # Deposit and Withdraw (normal methods)
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("withdraw", amount))
        else:
            print("Insufficient funds!")

    # Support len() and indexing
    def __len__(self):
        return len(self.transactions)

    def __getitem__(self, index):
        return self.transactions[index]

# Create two accounts
a1 = BankAccount("Alice", 1000)
a2 = BankAccount("Bob", 500)

# Deposit and withdraw
a1.deposit(200)
a1.withdraw(50)
a2.deposit(300)

print(a1)         # → Account(Alice) - Balance: $1150
print(a2)         # → Account(Bob) - Balance: $800

# Compare
print(a1 > a2)    # True → uses __lt__ reversed
print(a1 == a2)   # False

# Add accounts
a3 = a1 + a2
print(a3)         # → Account(Alice & Bob) - Balance: $1950

# Transactions
print(len(a1))    # → 2
print(a1[0])      # → ('deposit', 200)
