import unittest

from src.models.credit_account import CreditAccount

class TestCreditAccount(unittest.TestCase):
    def test_deposit(self):
        account = CreditAccount("1234567890", "John Doe", 1000, 500)
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)

    def test_withdraw(self):
        account = CreditAccount("1234567890", "John Doe", 1000, 500)
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 500)

    def test_withdraw_insufficient_credit_limit(self):
        account = CreditAccount("1234567890", "John Doe", 1000, 500)
        with self.assertRaises(ValueError):
            account.withdraw(1501)

    def test_to_dict(self):
        account = CreditAccount("1234567890", "John Doe", 1000, 500)
        dict = account.to_dict()
        self.assertEqual(dict['account_number'], "1234567890")
        self.assertEqual(dict['account_holder'], "John Doe")
        self.assertEqual(dict['balance'], 1000)
        self.assertEqual(dict['credit_limit'], 500)

if __name__ == '__main__':
    unittest.main()