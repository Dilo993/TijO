from abc import ABC, abstractmethod

class AbstractBankAccount(ABC):
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

class BankAccount(AbstractBankAccount):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise Exception("Insufficient funds")

class SavingsAccount(AbstractBankAccount):
    def withdraw(self, amount):
        if self._balance - amount >= 100:
            self._balance -= amount
        else:
            raise Exception("Minimum balance for savings account is 100")

def perform_transaction(account: AbstractBankAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)
    print(f"Balance after transaction: {account.get_balance()}")

regular_account = BankAccount()
savings_account = SavingsAccount()

perform_transaction(regular_account, 500, 200)
perform_transaction(savings_account, 500, 450)