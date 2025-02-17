import json
from account import Account


class AccountsManager:
    def __init__(self):
        # Dictionary to store accounts using account_number as key
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            raise ValueError("Account with this number already exists")
        self.accounts[account.account_number] = account

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            raise ValueError("Account not found")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            raise ValueError("Account not found")

    def deposit_to_account(self, account_number, amount):
        account = self.get_account(account_number)
        account.deposit(amount)

    def withdraw_from_account(self, account_number, amount):
        account = self.get_account(account_number)
        account.withdraw(amount)

    def get_all_accounts(self):
        return list(self.accounts.values())

    def save_to_file(self, filename):
        """Save all accounts to a JSON file."""
        data = [account.to_dict() for account in self.accounts.values()]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        """Load accounts from a JSON file."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            for account_data in data:
                account = Account.from_dict(account_data)
                self.accounts[account.account_number] = account
        except FileNotFoundError:
            pass  # It's okay if the file doesn't exist yet
