from typing import Dict
from src.models.db_account_manager import DbAccountManager
from src.models.credit_account import CreditAccount
from src.models.debit_account import DebitAccount
from src.models.account import Account, AccountType


class AccountController:
    def __init__(self, account_manager: DbAccountManager):
        self.account_manager: DbAccountManager = account_manager

    def create_account(
        self,
        account_type: str,
        account_number: str,
        holder: str,
        balance: float,
        limit: float,
    ) -> None:
        if account_type == "credit":
            account = CreditAccount(account_number, holder, balance, limit)
        else:
            account = DebitAccount(account_number, holder, balance, limit)

        self.account_manager.add_account(account)

    def update_account(self, account_number: str, holder: str, limit: float) -> None:
        acc = self.account_manager.get_account(account_number)
        if acc._account_type == AccountType.CREDIT:
            acc._credit_limit = limit
        else:
            acc._withdraw_limit = limit
        self.account_manager.update_account(acc)

    def delete_account(self, account_number: str) -> None:
        self.account_manager.delete_account(account_number)

    def perform_transaction(
        self, account_number: str, amount: float, transaction_type: str
    ) -> None:
        account = self.account_manager.get_account(account_number)
        if transaction_type == "deposit":
            account.deposit(amount)

        else:
            account.withdraw(amount)
        self.account_manager.update_account(account)

    def get_accounts(self) -> Dict[str, Account]:
        return self.account_manager.get_accounts()

    def get_account(self, account_number: str) -> Account:
        return self.account_manager.get_account(account_number)
