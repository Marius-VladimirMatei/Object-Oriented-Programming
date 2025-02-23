from typing import Dict
from src.models.account_manager import AccountManager
from src.models.credit_account import CreditAccount
from src.models.debit_account import DebitAccount
from src.models.account import Account


class AccountController:
    def __init__(self, account_manager: AccountManager):
        self.account_manager: AccountManager = account_manager

    def create_account(self, account_type: str, account_number: str,
                       holder: str, balance: float, limit: float) -> None:
        if account_type == "credit":
            account = CreditAccount(account_number, holder, balance, limit)
        else:
            account = DebitAccount(account_number, holder, balance, limit)

        self.account_manager.add_account(account)
        self.save_accounts()

    def update_account(self, account_number: str, holder: str, limit: float) -> None:
        self.account_manager.update_account(account_number, holder, limit)
        self.save_accounts()

    def delete_account(self, account_number: str) -> None:
        del self.account_manager._accounts[account_number]
        self.save_accounts()

    def perform_transaction(self, account_number: str, amount: float, transaction_type: str) -> None:
        account = self.account_manager._accounts[account_number]
        if transaction_type == "deposit":
            account.deposit(amount)
        else:
            account.withdraw(amount)
        self.save_accounts()

    def get_accounts(self) -> Dict[str, Account]:
        return self.account_manager._accounts

    def save_accounts(self) -> None:
        self.account_manager.save_accounts("accounts.json")
