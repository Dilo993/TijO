import unittest
import os,sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ATM import ATM,InvalidPinException,InsufficientFundsException

class ATM_test(unittest.TestCase):
    def test_check_balance(self):
        user_pin = 1234
        balance = 1000
        atm = ATM(user_pin, balance)
        self.assertEqual(atm.check_balance(user_pin), balance)
        self.assertRaises(InvalidPinException, atm.check_balance, 4321)

    def test_deposit(self):
        user_pin = 1234
        balance = 1000
        amount = 500
        atm = ATM(user_pin, balance)
        self.assertEqual(atm.deposit(user_pin, amount), balance + amount)
        self.assertRaises(InvalidPinException, atm.deposit, 4321, amount)

    def test_withdraw(self):
        user_pin = 1234
        balance = 1000
        amount = 500
        atm = ATM(user_pin, balance)
        self.assertEqual(atm.withdraw(user_pin, amount), balance - amount)
        self.assertRaises(InvalidPinException, atm.withdraw, 4321, amount)
        self.assertRaises(InsufficientFundsException, atm.withdraw, user_pin, balance + 1)