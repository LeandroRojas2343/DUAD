class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  # Represents the account balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} was deposited. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount} was withdrawn. Current balance: ${self.balance}")

# Class that inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=100):
        super().__init__(balance)  # Call to BankAccount constructor
        self.min_balance = min_balance  # Minimum allowed balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print(f"You can't withdraw ${amount}. Minimum balance required: ${self.min_balance}")
        else:
            self.balance -= amount
            print(f"${amount} was withdrawn. Current balance: ${self.balance}")
