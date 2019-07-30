from enum import Enum
from datetime import datetime

class InvalidDepositAmountError(Exception):
    pass

class InvalidWithdrawalAmountError(Exception):
    pass

class AccountStatus(Enum):
    Active = 1
    Inactive = 2
    Suspend = 3


class BankAccount():

    __slots__ = ("name", "__balance", "transactions", "__acct_id", "status")

    def __init__(self, name:str, balance:float = 0):
        self.__acct_id = self.generate_id()
        self.name = name
        self.__balance = balance
        self.transactions = []
        self.status = AccountStatus.Active

    @staticmethod
    def generate_id():
        return int(datetime.utcnow().timestamp() * 1000000)

    @property
    def acct_id(self):
        return self.__acct_id

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount<0:
            raise ValueError("Net balance must be 0 or more")

    def __repr__(self):
        return "id: {id} name: {name}, balance: {balance} status: {status}".format(
            id = self.__acct_id,
            name = self.name,
            balance = self.__balance,
            status = self.status
        )

    def deposit(self, amount):

        if not(type(amount) is int or type(amount) is float):
            raise InvalidDepositAmountError("Amount must be float or integer")

        if amount<0:
            raise InvalidDepositAmountError("Amount must be greater than 0")

        self.__balance = self.__balance + amount

    def withdraw(self, amount):

        if not(type(amount) is int or type(amount) is float):
            raise InvalidWithdrawalAmountError("Amount must be float or integer")

        if amount<0:
            raise InvalidWithdrawalAmountError("Amount must be greater than 0")

        if amount > self.__balance:
            raise InvalidWithdrawalAmountError("Withdrawal amount must be lower than the balance amount")

        self.__balance = self.__balance - amount

    def __eq__(self, other):
        return self.name == other.name