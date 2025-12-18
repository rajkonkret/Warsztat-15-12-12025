# hermetyzacja
from email.charset import add_codec


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # pole prywatne
        # name mangling
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("invalid or insufficient funds.")

    def get_balance(self):
        return self.__balance


account = BankAccount('Radek', 1000)
# AttributeError: 'BankAccount' object has no attribute '__balance'. Did you mean: 'get_balance'?
# po oznaczeniu jako pole prywatne nie można odczytac tego pola
# print(account.__balance)  # 1000
print(account.get_balance())
account.__balance = 2500  # publiczne pole o tej samej nazwie
# print(account.__balance)  # 2500
print(account.get_balance())
# 1000
# 1000

account.deposit(560)
print(account.get_balance())
account.withdraw(100)
print(account.get_balance())
# 1560
# 1460

# enkapsulacja - hermetyzowanie pol, dodawanie metod do odczytu i zapisu tych pól
