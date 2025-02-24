# import unittest
# from src.models.credit_account import CreditAccount
# from src.models.debit_account import DebitAccount
# import os


# class TestAccountManger(unittest.TestCase):
#     def test_add_account(self):
#         credit_account = CreditAccount("1234567890", "John Doe", 1000, 500)
#         account_manager = AccountManager()
#         account_manager.add_account(credit_account)
#         self.assertEqual(account_manager._accounts.__len__(), 1)
#         # to test assertEqual for other class attributes
#         self.assertEqual(
#             account_manager._accounts[credit_account._account_number]._balance, 1000
#         )

#         debit_account = DebitAccount("999999999", "Michale Jackson", 9099, 1344)
#         account_manager.add_account(debit_account)
#         self.assertEqual(account_manager._accounts.__len__(), 2)
#         self.assertEqual(
#             account_manager._accounts[debit_account._account_number]._account_holder,
#             "Michale Jackson",
#         )

#     def test_add_duplicate(self):
#         account_manager = (
#             AccountManager()
#         )  # instance needed to be created for testing duplicate accounts

#         debit_account = DebitAccount("999999999", "Michale Jackson", 9099, 1344)
#         debit_account_2 = DebitAccount(
#             "999999999", "Michale Jacwefwefwekson", 94356099, 13434564
#         )

#         account_manager.add_account(debit_account)

#         with self.assertRaises(ValueError):
#             account_manager.add_account(debit_account_2)

#     def test_save_accounts(self):
#         debit_account = DebitAccount("999999999", "Michael Jackson", 9099, 1344)
#         credit_account = CreditAccount("1234567890", "John Doe", 1000, 500)

#         account_manager = AccountManager()
#         account_manager.add_account(debit_account)
#         account_manager.add_account(credit_account)

#         account_manager.save_accounts("test_save_file.json")

#         self.assertTrue(os.path.exists("test_save_file.json"))

#     def test_load_accounts(self):
#         am = AccountManager.load_accounts("test_save_file.json")

#         self.assertEqual(am._accounts.__len__(), 2)
#         self.assertEqual(am._accounts["999999999"]._account_holder, "Michael Jackson")


# if __name__ == "__main__":
#     unittest.main()
