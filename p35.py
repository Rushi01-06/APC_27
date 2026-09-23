from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount:.2f} into Savings Account. New Balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f} from Savings Account. New Balance: ${self.balance:.2f}"
        return "Insufficient funds in Savings Account."

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount:.2f} into Current Account. New Balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        self.balance -= amount
        return f"Withdrew ${amount:.2f} from Current Account. New Balance: ${self.balance:.2f}"

if __name__ == "__main__":
    savings = SavingsAccount("SA101", 1000.0)
    current = CurrentAccount("CA202", 500.0)

    print(savings.deposit(250.0))
    print(savings.withdraw(200.0))
    print()
    print(current.deposit(1000.0))
    print(current.withdraw(1200.0))
