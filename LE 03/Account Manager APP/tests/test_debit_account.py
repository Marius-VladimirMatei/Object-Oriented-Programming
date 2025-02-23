import unittest
from src.models.debit_account import DebitAccount


# Unit tests in Python.
# We use the unittest library to create unit tests.
# We create a class that inherits from unittest.TestCase.
# This gives us access to self.assert* methods.
# In each test, we create an account object, call a method on the account,
# then test that the account's state is as expected.
#
# We can also use self.assertRaises to test that we raise exceptions.
class TestDebitAccount(unittest.TestCase):
    def test_deposit(self):
        account = DebitAccount("1234567890", "John Doe", 1000, 500)
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)

    def test_withdraw(self):
        account = DebitAccount("1234567890", "John Doe", 1000, 500)
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 500)

    def test_withdraw_insufficient_balance(self):
        account = DebitAccount("1234567890", "John Doe", 1000, 500)
        with self.assertRaises(ValueError):
            account.withdraw(1500)

    def test_withdraw_invalid_amount(self):
        account = DebitAccount("1234567890", "John Doe", 1000, 500)
        with self.assertRaises(ValueError):
            account.withdraw(-500)


if __name__ == '__main__':
    unittest.main()
