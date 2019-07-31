import unittest
import math
from bank_account import BankAccount, InvalidDepositAmountError, InvalidWithdrawalAmountError

"""
    Exercise: 
    1. write a test method to test equality of bank account record with another
    2. write a test method to test whether acct_id are unique when two records are created
    3. write a test method to verify the output of __repr__ function

"""

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("test bank account", 100)

    def test_default_balance(self):
        account = BankAccount("test bank account")
        self.assertTrue(account.balance == 0)

    def test_deposit(self):
        self.account.deposit(300)
        self.assertTrue(self.account.balance == 400)

        self.account.deposit(120.0)
        self.assertTrue(self.account.balance == 520.0)

    def test_withdrawal(self):
        self.account.withdraw(30)
        self.assertTrue(self.account.balance == 70.0)

        self.account.withdraw(30.3)
        self.assertTrue(math.isclose(self.account.balance, 39.7))


    def test_deposit_invalid_amount_type(self):
        with self.assertRaises(InvalidDepositAmountError) as err:
            self.account.deposit("2.3")
        with self.assertRaises(InvalidDepositAmountError) as err:
            self.account.deposit(True)


    def test_deposit_negative_amount(self):
        with self.assertRaises(InvalidDepositAmountError) as err:
            self.account.deposit(-2.3)
        with self.assertRaises(InvalidDepositAmountError) as err:
            self.account.deposit(-5)

    def test_withdrawal_invalid_amount_type(self):
        with self.assertRaises(InvalidWithdrawalAmountError) as err:
            self.account.withdraw("2.3")
        with self.assertRaises(InvalidWithdrawalAmountError) as err:
            self.account.withdraw(True)

    def test_withdrawal_negative_amount(self):
        with self.assertRaises(InvalidWithdrawalAmountError) as err:
            self.account.withdraw(-3.4)

    def test_withdrawal_insufficient_balance(self):
        with self.assertRaises(InvalidWithdrawalAmountError) as err:
            self.account.withdraw(1000)