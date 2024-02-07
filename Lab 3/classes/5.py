class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds!")

account1 = Account("Azamat", 100)

account1.deposit(1000)
account1.withdraw(1500)
account1.withdraw(1100)