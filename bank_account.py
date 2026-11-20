class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner #public
        self.__balance = balance #private

#getter:account balance
    @property
    def balance(self):
        return self.__balance 

#setter:account balance= value
    @balance.setter 
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

acc = BankAccount("John Doe", 1000)
acc.deposit(500)  # Deposited 500. New balance: 1500
acc.withdraw(200)  # Withdrew 200. New balance: 1300
print(acc.balance)  # Output: 1300

acc.balance = 2000  # Set new balance
print(acc.balance)  # Output: 2000

try:
    acc.balance = -100  # Attempt to set a negative balance
except ValueError as e:
    print(e)  # Output: Balance cannot be negative.

