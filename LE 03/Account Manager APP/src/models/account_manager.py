from src.models.account import Account, AccountType
from src.models.credit_account import CreditAccount
from src.models.debit_account import DebitAccount
import json


class AccountManager:
    def __init__(self):
        self._accounts: dict[str, Account] = {}

    def add_account(self, account: Account):
        if account._account_number in self._accounts:
            raise ValueError("This account already exists.")
        self._accounts[account._account_number] = account

    def update_account(self, account_number: str, new_holder: str, new_limit: float):
        if account_number not in self._accounts:
            raise ValueError("Account not found.")

        account = self._accounts[account_number]
        account._account_holder = new_holder

        if account._account_type == AccountType.CREDIT:
            account: CreditAccount = account
            account._credit_limit = new_limit
        else:
            account: DebitAccount = account
            account._withdraw_limit = new_limit

    # to do: remove account, update account???

    def save_accounts(self, file_name: str):
        data: dict[str, dict] = {}
        for _, account in self._accounts.items():
            data[account._account_number] = account.to_dict()

        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_accounts(file_name: str):
        am = AccountManager()  # Create an instance of AccountManager

        with open(file_name, "r") as f:
            data = json.load(f)

        for n, account in data.items():
            if account["account_type"] == "credit":
                a = CreditAccount(account["account_number"], account["account_holder"], account["balance"],
                                  account["credit_limit"])
            else:
                a = DebitAccount(account["account_number"], account["account_holder"], account["balance"],
                                 account["withdraw_limit"])

            am.add_account(a)  # Add the account to the AccountManager instance

        return am  # Return the AccountManager instance with all loaded accounts